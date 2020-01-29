from django.shortcuts import render
from .models import Player

# Create your views here.
def player_list(request):
    players = Player.objects.all().order_by('fname')
    return render(request, 'players/player_list.html', {'players':players})