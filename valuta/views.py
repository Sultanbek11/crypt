from django.http import JsonResponse
from rest_framework import viewsets, generics
from rest_framework import filters
from .models import Value
from .serializers import ValueSerializer
import requests
from bs4 import BeautifulSoup


class ValueListAPIView(generics.ListAPIView):
    queryset = Value.objects.all()
    serializer_class = ValueSerializer
    filter_backends = [filters.OrderingFilter]
    filterset_fields = ['id']


    # def get(self, request):
    #     url = 'https://bitinfocharts.com/ru/crypto-kurs/all.html'
    #     response = requests.get(url)
    #     soup = BeautifulSoup(response.text, 'html.parser')
    #     body = soup.find('div', {'class': 'ma-w1'})
    #     table = body.find('table', class_='table table-bordered table-condensed table-striped ma-w2 abtb')
    #     tbody = table.find('tbody')
    #     stroka = tbody.find_all('tr', class_='ptr')
    #     for x in stroka:
    #         changes_24h = x.find_all('td')
    #         change = changes_24h[1].find('span').find('b')
    #         name = changes_24h[0].find('span')
    #         price = changes_24h[1].find('a', class_='conv_cur')
    #         volume = changes_24h[4].find('span')
    #
    #         # Assign default values in case the values are not found
    #         change = change.text if change else '0.0'
    #         volume = volume.text if volume else '0.0'
    #         name = name.text if name else ''
    #         price = price.text if price else ''
    #
    #         # Use get_or_create to avoid the try-except block
    #         obj, created = Value.objects.get_or_create(title=name)
    #         obj.changes_12hour = change
    #         obj.price = price
    #         obj.volume = volume
    #         obj.save()
    #     return JsonResponse({'status': 'ok'})

class ValueRetriveAPIView(generics.RetrieveAPIView):
    queryset = Value.objects.all()
    serializer_class = ValueSerializer

class ValueViewSet(viewsets.ModelViewSet):
    queryset = Value.objects.all()
    serializer_class = ValueSerializer
    # permission_classes = IsAdminUser
    filter_backends = [filters.OrderingFilter]
    filterset_fields = ['price']