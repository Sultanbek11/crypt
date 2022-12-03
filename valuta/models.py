from django.db import models


# class Valuta(models.Model):
#     title = models.CharField(max_length=25)
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         verbose_name = "Валюты"
#         verbose_name_plural = "Валюты"


class Value(models.Model):
    # valut = models.OneToOneField(Valuta, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    volume = models.CharField(max_length=50, null=True)
    price = models.CharField(null=True, max_length=50)
    changes_12hour = models.CharField(null=True, max_length=50)


    @property
    def discount_in_percentage(self):
        return f"{self.changes_12hour} %"

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Значения валют"
        verbose_name_plural = "Значения валют"
        ordering = ('title',)
