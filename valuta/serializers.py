from rest_framework import serializers
from wallet.models import Wallet
from .models import Value


class ValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Value
        fields = ('id', 'title', 'price', 'volume', 'changes_12hour',)
