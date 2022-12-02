from rest_framework import serializers
from .models import Value, Valuta


class ParseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Valuta
        fields = '__all__'
