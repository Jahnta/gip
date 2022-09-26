from django.shortcuts import render, redirect, get_object_or_404
from .models import Station, Unit, Event, Contract, SparePartsList
from .forms import EventForm
from django.http import Http404
from django.contrib.auth.decorators import login_required, permission_required
import csv
import math
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, AccessMixin
# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def index2(request):
    return render(request, 'main/new_layout.html')


def event_detail(request, event_id):

    try:
        event = Event.objects.get(pk=event_id)
    except Event.DoesNotExist:
        raise Http404('Такой инспекции нет в базе данных.')

    try:
        spareparts = SparePartsList.objects.get(event=event)
        with open(spareparts.file.path, 'r', encoding='utf-8-sig', newline='') as csvfile:
            sp_reader = csv.reader(csvfile, delimiter=';')
            spareparts_list = list(sp_reader)
    except:
        spareparts_list = []
        spareparts = ''

    if not spareparts_list:
        spareparts_list_length = 0
    else:
        spareparts_list_length = len(set(x[0] for x in spareparts_list[1:] if x[0]))

    total = 0
    total_p = 0
    total_d = 0
    total_m = 0
    count = 0
    count_sum = 0

    try:
        x = spareparts_list[0].index('Статус') or 0
    except:
        x = 0

    try:
        y = spareparts_list[0].index('Поставщик')
    except:
        y = 0

    try:
        c = spareparts_list[0].index('Категория ВЕРХ')
    except:
        c = 0

    y_list = []

    for sparepart in spareparts_list[1:]:
        a = ''
        for s in sparepart[spareparts_list[0].index('Цена НИЗ')]:
            if s in '0123456789.,':
                a += s
        p = float(sparepart[spareparts_list[0].index('Кол-во НИЗ')].replace(',', '.') or 0) * float(a.replace(',', '.') or 0)
        total += p

        if sparepart[x] == ' Доставлено ' and sparepart[0]:
            count += 1
            count_sum += p

        if sparepart[y] not in y_list:
            y_list.append(sparepart[y])

        if sparepart[c] == 'Программные детали':
            total_p += p
        elif sparepart[c] == 'Другие детали':
            total_d += p
        elif sparepart[c] == 'Малые детали':
            total_m += p



    total_str = '{:,}'.format(round(total, 2))
    total_p_str = '{:,}'.format(round(total_p, 2))
    total_d_str = '{:,}'.format(round(total_d, 2))
    total_m_str = '{:,}'.format(round(total_m, 2))

    if spareparts_list_length != 0:
        count_percent = round(count * 100 / spareparts_list_length, 1)
    else:
        count_percent = 0

    if total != 0:
        count_sum_percent = round(count_sum * 100 / total, 1)
    else:
        count_sum_percent = 0

    data = {
        'event': event,
        'spareparts': spareparts,
        'spareparts_list' : spareparts_list,
        'spareparts_list_length' : spareparts_list_length,
        'spareparts_list_total' : total_str,
        'spareparts_list_total_p' : total_p_str,
        'spareparts_list_total_d' : total_d_str,
        'spareparts_list_total_m' : total_m_str,
        'count_percent' : count_percent,
        'count_sum_percent' : count_sum_percent,
        'y_list' : y_list,
    }

    return render(request, 'main/event_detail.html', data)

def chart(request):

    year_list = [x[0] for x in set(list(Event.objects.values_list('start__year')) + list(Event.objects.values_list('end__year')))]
    print(year_list)
    #year_list = [2022, 2023]
    years = []
    for year in sorted(year_list):
        stations = []
        station_list = Station.objects.all().order_by('number')
        for station in station_list:
            units = []
            unit_list = Unit.objects.order_by('short_name').filter(station=station)
            for unit in unit_list:
                event_list = []
                for event in Event.objects.order_by('start').filter(unit=unit):
                    if event.start.year == year or event.end.year == year:
                        event_list.append(event)
                unit_dict = {'unit' : unit, 'events' : event_list}
                units.append(unit_dict)
            station_dict = {'station' : station, 'units' : units}
            stations.append(station_dict)
        year_dict = {'year' : year, 'stations' : stations}
        years.append(year_dict)
    data = {'years' : years}

    return render(request, 'main/event_chart.html', data)

def stations(request):
    company_list = [x[0] for x in set(list(Station.objects.order_by('number').values_list('company')))]
    companies = []
    for company in sorted(company_list):
        stations = []
        station_list = Station.objects.filter(company=company)
        company_data = {
            'name' : company,
            'station_list' : station_list
        }
        companies.append(company_data)
    data = {
        'companies' : companies,
    }
    return render(request, 'main/station_all.html', data)

def station_detail(request, station_id):
    station = Station.objects.get(pk=station_id)
    unit_list = Unit.objects.filter(station__id=station_id)
    data = {
        'station' : station,
        'unit_list' : unit_list,
    }
    return render(request, 'main/station_detail.html', data)

def unit_detail(request, unit_id):
    unit = Unit.objects.get(pk=unit_id)
    event_list = Event.objects.filter(unit=unit).order_by('start')
    data = {
        'unit' : unit,
        'event_list' : event_list,
    }
    return render(request, 'main/unit_detail.html', data)

@login_required
@permission_required('main.add_event', raise_exception=False)
def create_card(request):
    error = ''
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('event_detail', event_id=post.pk)
        else:
            error = 'Форма заполнена неправильно'
    form = EventForm()
    data = {
        'form' : form,
        'error' : error,
    }
    return render(request, 'main/event_create.html', data)

@login_required
@permission_required('main.change_event', raise_exception=False)
def event_edit(request, event_id):
    error = ''
    post = get_object_or_404(Event, pk=event_id)
    if request.method == "POST":
        form = EventForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('event_detail', event_id=post.pk)
        else:
            error = 'Форма заполнена неправильно'
    else:
        form = EventForm(instance=post)
    data = {
        'form' : form,
        'error' : error,
    }
    return render(request, 'main/event_edit.html', data)

class EventDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'main.delete_event'
    model = Event
    success_url = reverse_lazy('chart')
    login_url = reverse_lazy('login')


    def handle_no_permission(self):
        return redirect(self.login_url)
