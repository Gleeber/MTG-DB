from django.http import HttpResponse
from django.shortcuts import render
from .models import Deck, Membership

# Create your views here.
def deck_list(request):
    decks = Deck.objects.all().order_by('name')
    return render(request, 'deck/deck_list.html', {'decks':decks})

def deck_info(request, id):
    deck = Deck.objects.get(id=id)
    memberships = Membership.objects.filter(deck__id=id).order_by('card__type')
    return render(request, 'deck/deck_info.html', {'deck':deck,'memberships':memberships})