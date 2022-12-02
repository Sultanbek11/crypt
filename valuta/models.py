from django.db import models


class Valuta(models.Model):
    title = models.CharField(max_length=25)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Валюты"
        verbose_name_plural = "Валюты"


class Value(models.Model):
    valut = models.OneToOneField(Valuta, on_delete=models.CASCADE)
    volume = models.DecimalField(max_digits=10, decimal_places=5)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    changes_12hour = models.DecimalField(max_digits=10, max_length=10, decimal_places=1)

    @property
    def discount_in_percentage(self):
        return f"{self.changes_12hour} %"

    class Meta:
        verbose_name = "Значения валют"
        verbose_name_plural = "Значения валют"
