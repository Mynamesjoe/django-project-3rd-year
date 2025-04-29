from django.urls import path
from . import views
from .views import CustomLoginView
from django.contrib.auth.views import LogoutView

app_name = 'users'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='users:login'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('artist/create/', views.artist_profile_create, name='artist-profile-create'),
    path('edit-artist-profile/artist', views.edit_artist_profile, name='edit_artist_profile'),
    path('client/create/', views.client_profile_create, name='client-profile-create'),
    path('edit-client-profile/artist', views.edit_client_profile, name='edit_client_profile'),
    path('dashboard/', views.dashboard_redirect, name='dashboard'),
    path('dashboard/artist/', views.artist_dashboard, name='artist_dashboard'),
    path('dashboard/client/', views.client_dashboard, name='client_dashboard'),
]