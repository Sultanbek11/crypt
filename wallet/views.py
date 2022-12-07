from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, generics
from rest_framework.permissions import IsAuthenticated
from users.models import Users
from .models import Wallet
from .serializers import WalletSerializer
from valuta.models import Value


class WalletViewSet(ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    permission_classes = (IsAuthenticated,)


class BuyValutAPIView(generics.CreateAPIView):
    queryset = Wallet.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = WalletSerializer

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=201, headers=headers)

        # super().post()
        # valut = Value.objects.get(id=kwargs['pk'])
        # user = request.user
        # sum = request.data.get('summ_in_dollar')
        # print(f'user-{user}')
        # print(f'valut-{valut}')
        # print(f'sum-{sum}')
        # wallet = user.wallet
        # wallet.update_(sum)
        # # balance_change = Wallet.objects.get(owners=user)
        # # balance_change.update_(sum)
        # # bal1 = WalletValutes(title_valute=valut, owner=Wallet.objects.get(owners=user))
        # # balance_change.save()
        # # bal1.save()
        # return Response({'text': 'ok'})
        # return Response(request.data)
        # valuta = get_object_or_404(Value, id=self.kwargs['pk'])
        # print(valuta)
        # wallet = Wallet.objects.update_or_create(owners=request.user,
        #                                           summ_in_dollar=request.data.get('summ_in_dollar'),
        #                                           title_valute=valuta)
        # serializer = BuyValuteSerializer(data=wallet)
        # if serializer.is_valid():
        #     # if not wallet:
        #     # print(serializer.data)
        #     serializer.save()
        #     wallet.save()
        #     data1 = Wallet(
        #         summ_in_dollar=serializer.data,
        #         owners=wallet,
        #         title_valute=valuta
        #     )
        #     # data1.objects.update_or_create(summ_in_dollar=serializer.data, owners=wallet, title_valute=valuta)
        #     data1.save()
        #     # return redirect('BuyAPIView.as_view()')
        #     return Response({'text': 'ok'})
        # return Response(request.data)
