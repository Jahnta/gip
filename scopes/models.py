from django.db import models

# Create your models here.

class Component(models.Model):
    name = models.CharField('Наименование компонента', max_length=100)

    def __str__(self):
        return self.name

class Scope(models.Model):
    component = models.ForeignKey(Component, on_delete=models.CASCADE, null=True)
    sow = models.TextField('Объем работ', max_length=500)
