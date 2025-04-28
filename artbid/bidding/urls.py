from django.urls import path
from . import views

urlpatterns = [
    path('artworks/', views.artwork_list, name='bidding_artwork_list'),
    path('artworks/<int:pk>/', views.artwork_detail_and_bid, name='artwork_detail_and_bid'),
]