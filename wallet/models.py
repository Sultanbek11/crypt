from uuid import uuid4

from django.core.mail import send_mail
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import Users
from valuta.models import Value


class Wallets(models.Model):
    owners = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    summ_in_dollar = models.DecimalField(decimal_places=3, max_digits=40, verbose_name='сумма', null=True)
    title_valute = models.ForeignKey(Value, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return str(self.owners)

class Transactions(models.Model):
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    summ = models.IntegerField()
    valut = models.ForeignKey(Value, on_delete=models.CASCADE)

    def __str__(self):
        return 'История транзакций'

class WalletsInfo(models.Model):
    token = models.UUIDField(default=uuid4)
    history_transactions = models.ForeignKey(Transactions, models.CASCADE)

    def __str__(self):
        return self.token

@receiver(post_save, sender=Users)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Wallets.objects.create(owners=instance)
