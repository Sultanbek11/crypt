from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, generics
from rest_framework.permissions import IsAuthenticated

from valuta.models import Value
from .models import Wallet, Purchase, WalletValutes, PurchaseInfo
from .serializers import WalletSerializer, BuyValuteSerializer


class WalletViewSet(ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    permission_classes = (IsAuthenticated,)


class BuyValutAPIView(generics.CreateAPIView):
    queryset = Purchase.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = BuyValuteSerializer
