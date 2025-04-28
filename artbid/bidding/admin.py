from django.contrib import admin
from .models import Bid, Winner

@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = ('artwork', 'client', 'bid_amount', 'bid_time')
    search_fields = ('artwork__title', 'client__user__username')
    list_filter = ('artwork',)

@admin.register(Winner)
class WinnerAdmin(admin.ModelAdmin):
    list_display = ('artwork', 'client', 'winning_bid', 'won_at')
    search_fields = ('artwork__title', 'client__user__username')