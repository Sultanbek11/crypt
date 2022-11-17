from django.db import models
from users.models import Users
from valuta.models import Valuta


class Account(models.Model):
    owners = models.ForeignKey(Users, on_delete=models.PROTECT)
    summ = models.IntegerField()
    count_valutes = models.ForeignKey(Valuta, on_delete=models.PROTECT)


class Desire(models.Model):
    first_sum = models.IntegerField()
    want_sum = models.IntegerField()
