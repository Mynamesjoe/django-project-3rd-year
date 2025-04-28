from django.db import models
from users.models import ArtistProfile

class Artwork(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='artworks/')
    starting_price = models.DecimalField(max_digits=10, decimal_places=2)
    artist = models.ForeignKey(ArtistProfile, on_delete=models.CASCADE)
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title