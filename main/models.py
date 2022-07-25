from django.db import models
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
    file = models.FileField('Файл договора', upload_to='uploads/')

    def __str__(self):
        return self.number

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
    start = models.DateField('Дата начала')
    end = models.DateField('Дата окончания')
    duration = models.IntegerField('Длительность', default=0)
    report = models.CharField('Номер отчета', max_length=50)
    contract = models.ForeignKey(Contract, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.short_name} {self.unit.short_name} {self.unit.station.short_name}'


