from django.urls import path
from . import views

urlpatterns = [
    path('', views.artwork_list, name='artwork_list'),
    path('<int:pk>/', views.artwork_detail, name='artwork_detail'),
    path('my/', views.my_artworks, name='my_artworks'),
    path('create/', views.artwork_create, name='artwork_create'),
    path('<int:pk>/edit/', views.artwork_update, name='artwork_update'),
    path('<int:pk>/delete/', views.artwork_delete, name='artwork_delete'),
]