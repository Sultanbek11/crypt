from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework import filters
from rest_framework.permissions import IsAdminUser
from .models import Value
from .serializers import ValueSerializer


class ValueListAPIView(generics.ListAPIView):
    queryset = Value.objects.all()
    serializer_class = ValueSerializer
    filter_backends = [filters.OrderingFilter]
    filterset_fields = ['id']

class ValueRetriveAPIView(generics.RetrieveAPIView):
    queryset = Value.objects.all()
    serializer_class = ValueSerializer
    # filter_backends = [filters.OrderingFilter]
    # filterset_fields = ['price']

class ValueViewSet(viewsets.ModelViewSet):
    queryset = Value.objects.all()
    serializer_class = ValueSerializer
    permission_classes = IsAdminUser
    filter_backends = [filters.OrderingFilter]
    filterset_fields = ['price']