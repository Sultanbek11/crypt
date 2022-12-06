import rest_framework.response
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet, generics
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from .models import Wallets
from .serializers import WalletSerializer
from valuta.models import Value
from .wallet import Wallet

class WalletViewSet(ModelViewSet):
    queryset = Wallets.objects.all()
    serializer_class = WalletSerializer
    permission_classes = (IsAuthenticated,)

class Wallet_add(generics.GenericAPIView):
    queryset = Wallets.objects.all()
    permission_classes = (IsAuthenticated, )

    def post(self, request, pk):
        valuta = get_object_or_404(Value, id=pk)
        print(f'валюта {valuta}')
        wallet = Wallets.objects.update(owners=request.user, title_valute=valuta)
        print(f'кошель {wallet}')
        if not wallet:
            wallet = Wallets(owners=request.user, title_valute=valuta)
            wallet.summ_in_dollar += 100
            wallet.save()
        return Response({'wallet':'wallet'})


# def basket_remove(request, pk):
#     content = {}
#     return render(request, 'basketapp/basket.html', content)