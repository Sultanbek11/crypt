from rest_framework import serializers

from .models import Wallet, Purchase, WalletValutes, PurchaseInfo


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('owner', 'summ_in_dollar')


class BuyValuteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ('amount', 'valuta', 'user')

