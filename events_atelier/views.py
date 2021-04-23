from django.shortcuts import render
from main_atelier.models import Events

# Create your views here.


def event_info(request, pk):
    event = Events.objects.get(pk=pk)
    return render(request, 'events.html', context={'event': event})
