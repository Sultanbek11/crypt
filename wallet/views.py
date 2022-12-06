from django.shortcuts import redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
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
        valuta = get_object_or_404(Value, id=self.kwargs['pk'])
        print(valuta)
        wallet = Wallets.objects.get(owners=request.user)
        # data = {'summ_in_dollar': request.data,
        #          'owners': wallet,
        #          'title_valute': valuta}
        serializer = BuyValuteSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            wallet.title_valute = valuta
            wallet.summ_in_dollar = serializer.data
            wallet.save()
            # return redirect('BuyAPIView.as_view()')
            return Response(serializer.data)
        return Response(serializer.data)

# class BuyAPIView(APIView):
#
#     def buy(self):
