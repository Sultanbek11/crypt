from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, generics
from rest_framework.permissions import IsAuthenticated
from .models import Wallet, Purchase, WalletValutes, PurchaseInfo, Sell
from .serializers import WalletSerializer, BuyValuteSerializer, SellValuteSerializer


class WalletViewSet(ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    permission_classes = (IsAuthenticated,)


class BuyValutAPIView(generics.CreateAPIView):
    queryset = Purchase.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = BuyValuteSerializer


class SellValutAPIView(generics.CreateAPIView):
    queryset = Sell.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = SellValuteSerializer

