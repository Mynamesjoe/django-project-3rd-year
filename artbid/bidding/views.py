from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from artworks.models import Artwork
from users.models import ClientProfile
from .models import Bid
from .forms import BidForm
from django.contrib import messages

# View: List all artworks (you may already have this in artworks app, but for flow, here it is)
def artwork_list(request):
    artworks = Artwork.objects.all().order_by('-created_at')
    return render(request, 'artworks/artwork_list.html', {'artworks': artworks})

# View: Detail of and bid on an artwork
@login_required
def artwork_detail_and_bid(request, pk):
    artwork = get_object_or_404(Artwork, pk=pk)
    bids = artwork.bids.all().order_by('-bid_amount')
    your_bid = None
    if request.user.is_authenticated and hasattr(request.user, "clientprofile"):
        your_bid = Bid.objects.filter(artwork=artwork, client=request.user.clientprofile).last()

    if request.method == 'POST':
        if not hasattr(request.user, "clientprofile"):
            messages.error(request, "Only clients can place bids.")
            return redirect('artwork_detail_and_bid', pk=pk)
        form = BidForm(request.POST)
        if form.is_valid():
            bid = form.save(commit=False)
            bid.artwork = artwork
            bid.client = request.user.clientprofile
            min_bid = artwork.starting_price
            highest_bid = bids.first().bid_amount if bids.exists() else min_bid
            if bid.bid_amount > highest_bid:
                bid.save()
                messages.success(request, "Your bid was placed!")
                return redirect('artwork_detail_and_bid', pk=pk)
            else:
                messages.error(request, f"Your bid must be higher than the current highest bid (${highest_bid}).")
    else:
        form = BidForm()
    return render(request, 'bidding/artwork_detail_and_bid.html', {
        'artwork': artwork,
        'form': form,
        'bids': bids,
        'your_bid': your_bid,
    })