from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet, generics
from rest_framework.permissions import IsAuthenticated
from .models import Wallets
from .serializers import WalletSerializer, BuyValuteSerializer
from valuta.models import Value


class WalletViewSet(ModelViewSet):
    queryset = Wallets.objects.all()
    serializer_class = WalletSerializer
    permission_classes = (IsAuthenticated,)


class Wallet_add(generics.GenericAPIView):
    queryset = Wallets.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = BuyValuteSerializer

    def post(self, request, *args, **kwargs):
        valuta = get_object_or_404(Value, id=request.pk)
        # summ = request.data
        # wallet = Wallets.objects.get(owners=request.user)
        serializer = BuyValuteSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            # wallet = Wallets.objects.update()
            # wallet.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data)
