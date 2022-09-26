from django.db import models

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