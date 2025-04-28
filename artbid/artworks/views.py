from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Artwork
from .forms import ArtworkForm

def artwork_list(request):
    artworks = Artwork.objects.all().order_by('-created_at')
    return render(request, 'artworks/artwork_list.html', {'artworks': artworks})

def artwork_detail(request, pk):
    artwork = get_object_or_404(Artwork, pk=pk)
    return render(request, 'artworks/artwork_detail.html', {'artwork': artwork})

@login_required
def artwork_create(request):
    if request.method == 'POST':
        form = ArtworkForm(request.POST, request.FILES)
        if form.is_valid():
            artwork = form.save(commit=False)
            artwork.artist = request.user.artistprofile  # Ensure each user has ArtistProfile
            artwork.save()
            return redirect('artwork_detail', pk=artwork.pk)
    else:
        form = ArtworkForm()
    return render(request, 'artworks/artwork_form.html', {'form': form})

@login_required
def artwork_update(request, pk):
    artwork = get_object_or_404(Artwork, pk=pk, artist=request.user.artistprofile)
    if request.method == 'POST':
        form = ArtworkForm(request.POST, request.FILES, instance=artwork)
        if form.is_valid():
            form.save()
            return redirect('artwork_detail', pk=artwork.pk)
    else:
        form = ArtworkForm(instance=artwork)
    return render(request, 'artworks/artwork_form.html', {'form': form})

@login_required
def artwork_delete(request, pk):
    artwork = get_object_or_404(Artwork, pk=pk, artist=request.user.artistprofile)
    if request.method == 'POST':
        artwork.delete()
        return redirect('artwork_list')
    return render(request, 'artworks/artwork_confirm_delete.html', {'artwork': artwork})


from django import forms
from .models import Artwork
from django.utils import timezone
from datetime import timedelta

class ArtworkForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        initial=(timezone.now() + timedelta(days=7)).strftime('%Y-%m-%dT%H:%M')
    )

    class Meta:
        model = Artwork
        fields = ['title', 'description', 'image', 'starting_price', 'deadline']


from django.contrib.auth.decorators import login_required

@login_required
def my_artworks(request):
    artworks = Artwork.objects.filter(artist=request.user.artistprofile)
    return render(request, 'artworks/artwork_list.html', {'artworks': artworks})