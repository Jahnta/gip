from django.shortcuts import render
from .models import Station, Unit, Event
from django.http import Http404

# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def cards(request):
    event_list = Event.objects.all().order_by('start')
    station_list = Station.objects.all().order_by('name')
    unit_list = Unit.objects.all().order_by('name')
    data = {
        'event_list' : event_list,
        'station_list' : station_list,
        'unit_list' : unit_list,
    }
    return render(request, 'main/cards.html', data)

def detail(request, event_id):
    try:
        event = Event.objects.get(pk=event_id)
    except Event.DoesNotExist:
        raise Http404('Такой инспекции нет в базе данных.')
    return render(request, 'main/detail.html', {'event': event})

def chart(request):
    return render(request, 'main/chart.html')
