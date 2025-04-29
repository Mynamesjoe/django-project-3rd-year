from django import forms
from .models import Artwork
from django.utils import timezone
from datetime import timedelta

class ArtworkForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        initial=timezone.now() + timedelta(days=7)  # Set initial value to 7 days from now
    )

    class Meta:
        model = Artwork
        fields = ['title', 'description', 'image', 'starting_price', 'deadline', 'category', 'dimensions', 'materials', 'status']
        labels = {
            'title': 'Artwork Title',
            'description': 'Description of the Artwork',
            'category': 'Category',
            'dimensions': 'Dimensions (e.g., 12x16 inches)',
            'materials': 'Materials Used',
            'status': 'Current Status',
            'starting_price': 'Starting Price ($)',
            'deadline': 'Auction Deadline',
        }
        help_texts = {
            'description': 'Provide a detailed description of the artwork.',
            'dimensions': 'Enter the dimensions in inches or centimeters (e.g., 12x16 inches).',
        }
        widgets = {
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(choices=Artwork.STATUS_CHOICES),
        }