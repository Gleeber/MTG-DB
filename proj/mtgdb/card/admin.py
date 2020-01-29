from django.contrib import admin
from .models import Card
from deck.admin import CardAdmin

admin.site.register(Card, CardAdmin)

class CardInLine(admin.TabularInline):
    model = Card

class ColorAdmin(admin.ModelAdmin):
    inlines = [
        CardInLine,
    ]