from .models import Value
from krypta.celery import app
import requests
from bs4 import BeautifulSoup


@app.task()
def parsing_value():
    print('Работает')
    url = 'https://bitinfocharts.com/ru/crypto-kurs/all.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    body = soup.find('div', {'class': 'ma-w1'})
    table = body.find('table', class_='table table-bordered table-condensed ma-w2 abtb')
    tbody = table.find('tbody')
    stroka = tbody.find_all('tr', class_='ptr')
    for x in stroka:
        try:
            changes_24h = x.find_all('td')
            change = changes_24h[1].find('span').find('b').text
            name = changes_24h[0].find('span').find('a').text
            price = changes_24h[1].find('a', class_='conv_cur').text
            volume = changes_24h[4].find('span').text
            # obj1 = Value.objects.create(title=name, changes_12hour=change, price=price, volume=volume)
            # obj1.save()
            obj = Value.objects.get(title=name)
            obj.changes_12hour = change
            obj.price = float(price)
            obj.volume = volume
            obj.save()
        except:
            change = '0.0'
            volume = '0.0'
            # obj1 = Value.objects.create(changes_12hour=change, volume=volume)
            # obj1.save()
            obj = Value.objects.get(title=name)
            obj.changes_12hour = change
            obj.volume = volume
            obj.save()
