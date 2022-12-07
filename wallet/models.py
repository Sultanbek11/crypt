from uuid import uuid4
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import Users


class Wallet(models.Model):
    owners = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='wallet')
    summ_in_dollar = models.DecimalField(decimal_places=3, max_digits=40, null=True)

    def __str__(self):
        return str(self.owners)

    def update_(self, new):
        self.summ_in_dollar += new
        self.save()


class WalletValutes(models.Model):
    title_valute = models.CharField(max_length=60, null=True)
    owner = models.ForeignKey(Wallet, on_delete=models.CASCADE)

    def __str__(self):
        return self.title_valute


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='order')
    valuta = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.valuta


class WalletInfo(models.Model):
    token = models.UUIDField(default=uuid4)
    history_transactions = models.ForeignKey(Order, models.CASCADE)

    def __str__(self):
        return self.token


@receiver(post_save, sender=Users)
def create_wallet(sender, instance, created, **kwargs):
    if created:
        Wallet.objects.create(owners=instance)

@receiver(post_save, sender=Order)
def add_to_wallet(sender, instance, created, **kwargs):
    if created:


