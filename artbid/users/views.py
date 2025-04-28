from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ArtistProfileForm, ClientProfileForm
from .models import ArtistProfile, ClientProfile
from django.contrib.auth.views import LoginView
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            username = form.cleaned_data.get('username')
            role = form.cleaned_data.get('role')
            messages.success(request, f'Account created for {username}! You can now login.')
            if role == 'artist':
                return redirect('users:artist-profile-create') # No user_id required, see below
            elif role == 'client':
                return redirect('users:client-profile-create')
            else:
                return redirect('login')
        # fall-through so errors render form
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def artist_profile_create(request):
    """Create Artist Profile for the current logged-in user only."""
    if hasattr(request.user, "artistprofile"):
        messages.info(request, "You already have an artist profile.")
        return redirect('users:profile')
    if request.method == 'POST':
        form = ArtistProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user  # associate with current user
            profile.save()
            messages.success(request, 'Artist profile created successfully!')
            return redirect('users:profile')
    else:
        form = ArtistProfileForm()
    return render(request, 'users/artist_profile_create.html', {'form': form})

@login_required
def client_profile_create(request):
    """Create Client Profile for the current logged-in user only."""
    if hasattr(request.user, "clientprofile"):
        messages.info(request, "You already have a client profile.")
        return redirect('users:profile')
    if request.method == 'POST':
        form = ClientProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, 'Client profile created successfully!')
            return redirect('users:profile')
    else:
        form = ClientProfileForm()
    return render(request, 'users/client_profile_create.html', {'form': form})

@login_required
def profile(request):
    if request.user.role == 'artist':
        try:
            artist_profile = request.user.artistprofile
        except ArtistProfile.DoesNotExist:
            return redirect('users:artist-profile-create')
        form = ArtistProfileForm(instance=artist_profile)
    elif request.user.role == 'client':
        try:
            client_profile = request.user.clientprofile
        except ClientProfile.DoesNotExist:
            return redirect('users:client-profile-create')
        form = ClientProfileForm(instance=client_profile)
    else:
        form = None

    if request.method == 'POST':
        if request.user.role == 'artist':
            form = ArtistProfileForm(request.POST, request.FILES, instance=artist_profile)
        elif request.user.role == 'client':
            form = ClientProfileForm(request.POST, instance=client_profile)
        if form and form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('users:login')
    return render(request, 'users/profile.html', {'form': form})

def home(request):
    user_id = request.user.id if request.user.is_authenticated else None
    return render(request, 'home.html', {'user_id': user_id})

class CustomLoginView(LoginView):
    template_name = 'users/login.html'

@login_required
def dashboard_redirect(request):
    user = request.user
    if user.role == "artist":
        return redirect('users:artist_dashboard')
    elif user.role == "client":
        return redirect('users:client_dashboard')
    else:
        return redirect('home')

@login_required
def artist_dashboard(request):
    return render(request, 'users/artist_dashboard.html')

# users/views.py
from artworks.models import Artwork

@login_required
def client_dashboard(request):
    artworks = Artwork.objects.all()  # Or apply filters if you want!
    return render(request, 'users/client_dashboard.html', {'artworks': artworks})