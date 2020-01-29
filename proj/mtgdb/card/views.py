from django.shortcuts import render
from .models import Card

# Create your views here.
def card_list(request):
    cards = Card.objects.all().order_by('name')
    return render(request, 'card/card_list.html', {'cards':cards})