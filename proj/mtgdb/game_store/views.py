from django.shortcuts import render
from .models import GameStore

# Create your views here.
def game_store_list(request):
    game_stores = GameStore.objects.all().order_by('name')
    return render(request, 'game_store/game_store_list.html', {'game_stores':game_stores})

def game_store_info(request, id):
    game_store = GameStore.objects.get(id=id)
    return render(request, 'game_store/game_store_info.html', {'game_store':game_store})