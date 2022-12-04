from django.db import models
from users.models import Users
from valuta.models import Value


class Account(models.Model):
    owners = models.ForeignKey(Users, on_delete=models.PROTECT)
    summ_in_dollar = models.DecimalField(decimal_places=3, max_digits=40)
    title_valute = models.ForeignKey(Value, on_delete=models.PROTECT)

    def __str__(self):
        return self.owners

# class Desire(models.Model):
#     first_sum = models.IntegerField()
#     want_sum = models.IntegerField()
