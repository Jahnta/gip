from django.db import models
from scopes.models import Scope
import datetime

# Create your models here.

class Contract(models.Model):
    number = models.CharField('Номер договора', max_length=50)
    reg_date = models.DateField('Дата договора')
    group = models.CharField('Группа договоров', max_length=50)
    subject = models.TextField('Предмет договора', max_length=500)
    value_rub = models.DecimalField('Цена договора в валюте', decimal_places=2, max_digits=15)
    value_cur = models.DecimalField('Цена договора в рублях', decimal_places=2, max_digits=15)
    counterparty = models.CharField('Контрагент', max_length=500)
    file = models.FileField('Файл договора', null=True, upload_to='', blank=True)
    contract_type = models.CharField('Тип договора', max_length=2, choices=[('Д', 'Доходный'), ('Р', 'Расходный')], default='Доходный')

    def __str__(self):
        return f'{self.number} от {self.reg_date}'

class Station(models.Model):
    name = models.CharField('Наименование станции', max_length=100)
    short_name = models.CharField('Короткое наименование станции', max_length=10, default='-')
    number = models.IntegerField('Ид.', default=0, null=True, blank=True)
    company = models.CharField('Генерирующая компания', max_length=50, null=True, blank=True)
    image = models.ImageField('Изображение', blank=True, upload_to='')
    address = models.CharField('Адрес нахождения', max_length=100, null=True, blank=True)
    text = models.CharField('Текст', max_length=100, null=True, blank=True)
    large_text = models.TextField('Большой текст', max_length=2000, null=True, blank=True)

    def __str__(self):
        return self.name

class UnitType(models.Model):
    machine_type = models.CharField('Тип машины', max_length=50, default='Газотурбинная установка')
    name = models.CharField('Имя установки', max_length=10, default='-')

    def __str__(self):
        return self.machine_type + ' ' + self.name

class Unit(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    name = models.CharField('Наименование установки', max_length=100)
    short_name = models.CharField('Короткое наименование установки', max_length=10, default='-')
    unit_type = models.ForeignKey(UnitType, on_delete=models.SET_NULL, null=True, blank=True)
    station_number = models.CharField('Станционный номер', max_length=10, null=True, blank=True)

    def __str__(self):
        return self.short_name + ' ' + self.station.short_name

class EventType(models.Model):
    full_name = models.CharField('Полное наименование события', max_length=100, null=True, blank=True)
    short_name = models.CharField('Короткое наименование события', max_length=10, null=True, blank=True)

    def __str__(self):
        return self.short_name

class UnitEventType(models.Model):
    unit_type = models.ForeignKey(UnitType, on_delete=models.CASCADE)
    event_type = models.ForeignKey(EventType, on_delete=models.SET_NULL, null=True, blank=True)
    default_duration = models.IntegerField('Типовая длительность', default=7)

    def __str__(self):
        return self.event_type.short_name + ' ' + self.unit_type.name


class Event(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    event_type = models.ForeignKey(UnitEventType, on_delete=models.SET_NULL, null=True, blank=True)
    short_name = models.CharField('Короткое имя события', max_length=10)
    full_name = models.CharField('Полное имя события', max_length=100)
    start = models.DateField('Дата начала')
    end = models.DateField('Дата окончания')
    duration = models.IntegerField('Длительность', default=0)
    report = models.CharField('Номер отчета', max_length=50, null=True, blank=True, default='-')
    contract = models.ForeignKey(Contract, null=True, on_delete=models.SET_NULL, blank=True)
    report_file = models.FileField('Файл отчета', upload_to='', null=True, blank=True)

    def __str__(self):
        return f'{self.short_name} {self.unit.short_name} {self.unit.station.short_name}'

class SparePartsList(models.Model):
    file = models.FileField('Файл CSV запасных частей', blank=True, upload_to='')
    event = models.ForeignKey(Event, null=True , on_delete=models.SET_NULL)

    def __str__(self):
        return f'Запчасти для {self.event}'

class EventScope(models.Model):
    pass
