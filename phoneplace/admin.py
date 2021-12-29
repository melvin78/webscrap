from django.contrib import admin
import requests
from bs4 import BeautifulSoup

from subcategory.models import SubCategory
from tracker.models import Tracker


class ScrapPhoneplace:
    fin = []

    def trackprice(self, link):
        res = requests.get(link)
        sp = BeautifulSoup(res.content, 'lxml')

        allphones = sp.find('ul', {"class": ["products", "columns-4", " columns__wide--5"]})
        phones = allphones.find_all("span", {"class": "gtm4wp_productdata"})

        for g in phones:
            data = {
                "name": g.attrs.get("data-gtm4wp_product_name"),
                "price": float(g.attrs.get("data-gtm4wp_product_price")),
                "link": g.attrs.get("data-gtm4wp_product_url")

            }
            self.fin.append(data)
        return self.fin

    def allPrices(self):
        return list(SubCategory.objects.filter(link__icontains='phoneplacekenya').values('name', 'current_price'))


class new_data_phoneplace:
    def update_db(self, name, price):
        ids = SubCategory.objects.filter(name=name).values_list('idsub_category', flat=True)

        oldprice = Tracker.objects.filter(subcategory_id=ids[0])
        if oldprice:
            if oldprice.values('price').latest('created_at')['price'] != price:
                Tracker.objects.create(
                    subcategory_id=ids[0],
                    price=price
                )
            else:
                print('web price is' + str(price) + 'and old price' + str(oldprice))
        else:

            Tracker.objects.create(
                subcategory_id=ids[0],
                price=price
            )
