from django import forms
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'unit',
            'short_name',
            'full_name',
            'start',
            'end',
            'duration'
        ]
        labels = {
            'unit' : 'Установка',
        }


