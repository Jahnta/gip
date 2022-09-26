from django.contrib import admin
from .models import Station, Unit, Event, Contract, SparePartsList, EventType, UnitType, UnitEventType
from scopes.admin import ScopeInLine, ScopeAdmin
# Register your models here.

class UnitInLine(admin.TabularInline):
    model = Unit
    extra = 1
    ordering = ('name',)

class EventInLine(admin.TabularInline):
    model = Event
    extra = 1
    ordering = ('start',)

class StationAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_name', 'number', 'company')
    fieldsets = [
        ('Информация о станции',
         {'fields' : [
             'company',
             'name',
             'short_name',
             'number',
             'image',
             'address',
             'text',
             'large_text',
         ]}),
    ]
    ordering = ('number',)
    inlines = [UnitInLine]

class UnitAdmin(admin.ModelAdmin):
    list_filter = ['station']
    list_display = ('name', 'short_name', 'station')
    ordering = ('station', 'name')
    inlines = [EventInLine]

class EventTypeAdmin(admin.ModelAdmin):
    list_display = ('short_name', 'full_name')

class UnitEventTypeAdmin(admin.ModelAdmin):
    list_display = ('event_type', 'unit_type')
    list_filter = ['unit_type']


class EventAdmin(admin.ModelAdmin):
    list_filter = ['unit']
    list_display = ('full_name', 'unit', 'start', 'end', 'report_file')

class ContractAdmin(admin.ModelAdmin):
    list_filter = ['counterparty']
    list_display = ('number', 'reg_date', 'counterparty',)
    ordering = ('number',)

admin.site.register(Station, StationAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(SparePartsList)
admin.site.register(EventType, EventTypeAdmin)
admin.site.register(UnitType)
admin.site.register(UnitEventType, UnitEventTypeAdmin)