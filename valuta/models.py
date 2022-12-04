from django.db import models


class Value(models.Model):
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
