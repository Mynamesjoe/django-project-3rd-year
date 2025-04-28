from django.db import models
from artworks.models import Artwork
from users.models import ClientProfile

class Bid(models.Model):
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE, related_name='bids')
    client = models.ForeignKey(ClientProfile, on_delete=models.CASCADE)
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    bid_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client.user.username} - {self.bid_amount}"

class Winner(models.Model):
    artwork = models.OneToOneField(Artwork, on_delete=models.CASCADE)
    client = models.ForeignKey(ClientProfile, on_delete=models.CASCADE)
    winning_bid = models.DecimalField(max_digits=10, decimal_places=2)
    won_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Winner: {self.client.user.username} for {self.artwork.title}"