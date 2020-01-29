from django.http import HttpResponse
from django.shortcuts import render
from .models import Event
from match.models import Match

# Create your views here.
def event_list(request):
    events = Event.objects.all().order_by('name')
    return render(request, 'event/event_list.html', {'events':events})

def event_info(request, id):
    event = Event.objects.get(id=id)
    matches = event.match_set.all()
    for eachMatch in matches:
        print(eachMatch.winner)
        # if eachMatch.winner is None:
        #     eachMatch.winner = "Tie"
    return render(request, 'event/event_info.html', {'event':event,'matches':matches})