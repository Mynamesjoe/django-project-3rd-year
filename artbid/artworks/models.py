from django.db import models
from users.models import ArtistProfile

class Artwork(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('sold', 'Sold'),
        ('under_auction', 'Under Auction'),
        ('reserved', 'Reserved'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='artworks/')
    starting_price = models.DecimalField(max_digits=10, decimal_places=2)
    artist = models.ForeignKey(ArtistProfile, on_delete=models.CASCADE)
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    # New fields
    category = models.CharField(max_length=100, blank=True, null=True)  # e.g., Painting, Sculpture
    dimensions = models.CharField(max_length=100, blank=True, null=True)  # e.g., 12x16 inches
    materials = models.CharField(max_length=200, blank=True, null=True)  # e.g., Oil on canvas, Bronze

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='available',
    )

    def __str__(self):
        return self.title