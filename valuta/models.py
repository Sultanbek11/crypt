from django.db import models


class Valuta(models.Model):
    title = models.CharField(max_length=25)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Валюты"


class Value(models.Model):
    volume = models.DecimalField(max_digits=10, decimal_places=5)

    class Meta:
        verbose_name = "Значения валют"
