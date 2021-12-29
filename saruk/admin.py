from django.contrib import admin

# Register your models here.

# from subcategory.models import SubCategory


import requests
from tracker.models import Tracker
from bs4 import BeautifulSoup

from subcategory.models import SubCategory


class ScrapSaruk:
    fin = []

    def trackprice(self, link):

        res = requests.get(link)
        sp = BeautifulSoup(res.content, 'lxml')

        all_laptops = sp.find('div', {"class": ["seasonproducts", " productsdisplay"]}) \
            .find('div', {"class": ["tablediv", "paginatedcontent"]}) \
            .find_all("div", {"class": "tablecelldiv"})

        for g in all_laptops:
            if not g.find("div", {"class": "itemname"}).string:
                name = ''
            else:
                name = g.find("div", {"class": "itemname"}).string
            if not g.find("div", {"class": "itemprice"}).text[4:].replace(',', '').replace('.', ''):
                price = 0
            else:
                price = float(g.find("div", {"class": "itemprice"}).text[4:].replace(',', '').replace('.', ''))

            data = {
                "name": name,
                "price": price,
                "link": 'https://saruk.co.ke/' + link,
                "image": 'https://saruk.co.ke/' + g.find("img").attrs.get('src')

            }
            if not data['name'] == '':
                self.fin.append(data)
        return self.fin

    def allPrices(self):
        return list(SubCategory.objects.filter(link__icontains='saruk').values('name', 'current_price'))


class new_data_saruk:
    def update_db(self, name, price):
        # formatname = name.replace('.', '')
        ids = SubCategory.objects.filter(name=name).values_list('idsub_category', flat=True)

        oldprice = Tracker.objects.filter(subcategory_id=ids[0])
        if oldprice:
            if oldprice.values('price').latest('created_at')['price'] != price:
                Tracker.objects.create(
                    subcategory_id=ids[0],
                    price=price
                )
            else:
                print('nothings changed')
        else:

            Tracker.objects.create(
                subcategory_id=ids[0],
                price=price
            )
