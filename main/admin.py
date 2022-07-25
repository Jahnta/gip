from django.contrib import admin
from .models import Station, Unit, Event, Contract
# Register your models here.

admin.site.register(Station)
admin.site.register(Unit)
admin.site.register(Event)
admin.site.register(Contract)