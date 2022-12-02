import requests
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, viewsets
from bs4 import BeautifulSoup
from .models import Valuta, Value
from .serializers import ParseSerializer


class ValutaListAPIView(APIView):
    # def get(self, request):
    #     url = 'https://myfin.by/crypto-rates'
    #     response = requests.get(url)
    #     soup = BeautifulSoup(response.text, 'html.parser')
    #     container_back = soup.find('div', class_='container background')
    #     with open('log1.html', 'w') as f:
    #         f.write(response.text)
    #     workarea = container_back.find('article', {'id': 'workarea'})
    #     content_table = workarea.find('div', class_='content_i rates-table')
    #     table = content_table.find('div', class_='rates-table-nbrb crypto_currency')
    #     items_table = table.find('table', class_="items")
    #     body_table = items_table.find('tbody', class_='table-body')
    #     value_crypto = body_table.find('tr')
    #     part_name = value_crypto.find('div', class_='names')
    #     name = part_name.find('a', class_='s-bold').text
    #     value = value_crypto.find_all('td')
    #     print(f'имя{value[1].text}')
    #     print(name)
    #
    #     serializer = ParseSerializer(data=name)
    #     serializer.is_valid()

    # def get(self, request):
    #     url = 'https://alpari.com/ru/markets/crypto/'
    #     response = requests.get(url)
    #     soup = BeautifulSoup(response.text, 'html.parser')
    #     container_back = soup.find('div', class_='markets--crypto__table -app-section -app-section_shadow -app-section_gap -app-section_background_white')
    #     with open('log1.html', 'w') as f:
    #         f.write(response.text)
    #     workarea = container_back.find('div', class_='-adaptive-table')
    #     content_table = workarea.find('table', class_='-adaptive-table__table')
    #     stroka = content_table.find_all('tr', class_='-adaptive-table__tr')
    #     for x in stroka:
    #         name = x.find('td', class_="-adaptive-table__td -adaptive-table__td_content-align-left").text
    #         changes_24h = x.find_all('td', {"class": "-adaptive-table__td -adaptive-table__td_content-align-right"})
    #         change = changes_24h[0]
    #         price = changes_24h[1]
    #         vloume = changes_24h[2]
    #         market_cap = changes_24h[3]
    #
    #         print(name, price, change.text, vloume.text, market_cap.text)
    #
    #         serializer = ParseSerializer(data=name)
    #         serializer.is_valid()
    #
    #     return Response({'text': 'ok'})

    # def get(self, request):
    #     url = 'https://coinmarketcap.com/'
    #     response = requests.get(url)
    #     soup = BeautifulSoup(response.text, 'html.parser')
    #     # print(soup)
    #     start = soup.find('body', class_='DAY')
    #     columns = start.find('div', class_='sc-c5c9d167-1 iZIMUr')
    #     print(columns)
    #     with open('log1.html', 'w') as f:
    #         f.write(response.text)
    #     content = columns.find('div', class_='columns_content')
    #     con = content.find('div', class_='sc-1a736df3-0 PimrZ cmc-body-wrapper')
    #     con2 = con.find('div', class_='grid')
    #     con3 = con2.find('div', class_='sc-f7a61dda-2 efhsPu')
    #     table = con3.find('table', class_='sc-f7a61dda-3 kCSmOD cmc-table')
    #     stroka = table.find_all('tr')
    #     # print(stroka)
    #     for x in stroka:
    #         changes_24h = x.find_all('td')
    #         change = changes_24h[5]
    #         price = changes_24h[1]
    #         vloume = changes_24h[2]
    #         market_cap = changes_24h[3]
    #         print(changes_24h)
    #         print(change)
    #         print(price, change.text, vloume.text, market_cap.text)
    #
    #         serializer = ParseSerializer(data=changes_24h)
    #         serializer.is_valid()
    #
    #     return Response({'text': 'ok'})

    def get(self, request):
        url = 'https://www.banknn.ru/kurs-kriptovalyut'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        contnainer = soup.find('div', class_='container')
        columns = contnainer.find('div', class_='columns')
        print(columns)
        with open('log1.html', 'w') as f:
            f.write(response.text)
        main = columns.find('main', class_='column-left')
        form = main.find('form', class_='m-b-4')
        table = form.find('table', class_='table table-hover table-crypto')
        stroka = table.find_all('tr')
        for x in stroka:
            changes_24h = x.find_all('td')
            name = x.find('div')
            change = changes_24h[4]
            price = changes_24h[3]
            vloume = changes_24h[2]
            market_cap = changes_24h[1]
            print(f'name{name}')
            print(f'change{change}')
            print(f'price{price}')
            print(f'volume{vloume}')
            print(f'capit{market_cap}')

        serializer = ParseSerializer(data=stroka)
        serializer.is_valid()

        return Response({'text': 'ok'})
