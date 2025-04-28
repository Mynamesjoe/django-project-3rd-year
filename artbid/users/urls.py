from django.urls import path
from . import views
from .views import CustomLoginView

app_name = 'users'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('profile/', views.profile, name='profile'),
    path('artist/create/', views.artist_profile_create, name='artist-profile-create'),
    path('client/create/', views.client_profile_create, name='client-profile-create'),  # <-- FIXED!
    path('dashboard/', views.dashboard_redirect, name='dashboard'),
    path('dashboard/artist/', views.artist_dashboard, name='artist_dashboard'),
    path('dashboard/client/', views.client_dashboard, name='client_dashboard'),
]