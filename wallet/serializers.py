from rest_framework import serializers
from .models import Wallets


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallets
        fields = ('owners', 'summ_in_dollar', 'title_valute')
