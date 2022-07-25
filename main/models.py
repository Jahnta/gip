from django.db import models
import datetime

# Create your models here.

class Station(models.Model):
    name = models.CharField('Наименование станции', max_length=100)
    short_name = models.CharField('Короткое наименование станции', max_length=10, default='-')

    def __str__(self):
        return self.name

class Unit(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    name = models.CharField('Наименование установки', max_length=100)
    short_name = models.CharField('Короткое наименование установки', max_length=10, default='-')

    def __str__(self):
        return self.short_name + ' ' + self.station.short_name

class Event(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    short_name = models.CharField('Короткое имя события', max_length=10)
    full_name = models.CharField('Полное имя события', max_length=100)
    start = models.DateTimeField()
    end = models.DateTimeField()
    duration = models.IntegerField()
    contract = models.CharField('Номер и дата договора', max_length=50)
    report = models.CharField('Номер отчета', max_length=50)

    def __str__(self):
        return f'{self.short_name} {self.unit.short_name} {self.unit.station.short_name}'