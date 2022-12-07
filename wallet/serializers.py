from urllib import request

from rest_framework import serializers
from .models import Wallet


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('owners', 'summ_in_dollar')


# class BuyValuteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Wallet
#         fields = ('summ_in_dollar', 'title_valute', 'owners')
#
#     # def save(self, **kwargs):
#     #     owner = Wallet(
#     #         owners=self.validated_data['owners'],
#     #         summ_in_dollar=self.validated_data['summ_in_dollar'],
#     #         title_valute=self.validated_data['title_valute'],
#     #     )
#     #     owner.save()
#     #     return owner



