from urllib import request

from rest_framework import serializers
from .models import Wallets


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallets
        fields = ('owners', 'summ_in_dollar', 'title_valute')


class BuyValuteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallets
        fields = ('summ_in_dollar', 'title_valute', 'owners')

    # def save(self, **kwargs):
    #     owner = Wallets(
    #         owners=self.validated_data['owners'],
    #         summ_in_dollar=self.validated_data['summ_in_dollar'],
    #         title_valute=self.validated_data['title_valute'],
    #     )
    #     owner.save()
    #     return owner



