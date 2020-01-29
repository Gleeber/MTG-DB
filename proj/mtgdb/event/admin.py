from django.contrib import admin
from .models import Event
from match.models import Match

class MatchInLine(admin.TabularInline):
    model = Match

class EventAdmin(admin.ModelAdmin):
    inlines = [
        MatchInLine,
    ]

# Register your models here.
admin.site.register(Event, EventAdmin)