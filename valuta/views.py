from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework import filters
from .models import Value
from .serializers import ValueSerializer


class ValueViewSet(viewsets.ModelViewSet):
    queryset = Value.objects.all()
    serializer_class = ValueSerializer
    filter_backends = [filters.OrderingFilter]
    filterset_fields = ['price']
