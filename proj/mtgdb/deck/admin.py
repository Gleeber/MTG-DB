from django.contrib import admin
from .models import Deck, Membership
from card.models import Card

class MembershipInline(admin.TabularInline):
    model = Membership
    extra = 1

class DeckAdmin(admin.ModelAdmin):
    inlines = [
        MembershipInline,
    ]

class CardAdmin(admin.ModelAdmin):
    inlines = [
        MembershipInline,
    ]

admin.site.register(Membership)
admin.site.register(Deck, DeckAdmin)