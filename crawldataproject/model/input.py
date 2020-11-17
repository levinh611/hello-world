from peewee import Model, CharField, IntegerField, DateTimeField, ForeignKeyField, BooleanField, TextField, JOIN, fn, FloatField
from crawldataproject.model import BaseModel
import requests
import re
from crawldataproject.model.sosanh import SoSanh
from crawldataproject.model.data import Data
from datetime import datetime
import time

class Input(BaseModel):
    id = IntegerField(primary_key=True)
    url = CharField()
    website = CharField()
    status = CharField()
    @classmethod
    def init_log(cls, **kwargs):
        return cls.insert(
            url=kwargs.get("url"),
            website=kwargs.get("website"),
            status = kwargs.get("status")
        ).execute()
    @classmethod
    def search(cls):
        data = cls.select(cls.id, cls.url , cls.website, cls.status).dicts()
        return [i for i in data]

    @classmethod
    def get_list_input(cls, **kwargs):
        h = cls.select(cls.id, cls.url, cls.website,cls.status).dicts()
        keyword = kwargs.get("keyword")
        if keyword:
            a = h.where(cls.website.contains(keyword))

            status = kwargs.get("status", 'ok')
            b = a.where(cls.status == status)

            page_size = kwargs.get("page_size", 10)
            c = b.limit(int(page_size))

            page_index = kwargs.get("page_index", 0)
            data = c.offset(int(page_index))


        return [i for i in data]

for input in Input.select():
    url = input.url
    website = input.website
    status = input.status
    start = datetime.now()
    if website == 'Sendo' and status == 'ok':
        page = requests.get(url)
        page1 = page.content
        links1 = re.findall('<strong class="currentPrice_2zpf">(.*?)</strong>', str(page1))
        a = links1[0][:6].split('.')
        b = int(''.join(a))
        sendo1 = {"time":start,"productid":123,"name": 'cafe G7',"price":b,"url":url,"website":'Sendo'}
        sendo2 = {"productid":123,"name": 'cafe G7',"price":b,"url":url,"website":'Sendo'}
        SoSanh.insert(sendo1).execute()
        Data.insert(sendo2).execute()
    if website == 'Shoppe'and status == 'ok':
        r = requests.get(url).json()
        productid = 123
        name = 'cafe G7'
        price = int(r['item']['price']) // 100000
        website = 'Shoppe'
        shoppe1 = {"time":start,"productid":productid,"name":name,"price":price,"url":url,"website":website}
        shoppe2={"productid":productid,"name":name,"price":price,"url":url,"website":website}
        SoSanh.insert(shoppe1).execute()
        Data.insert(shoppe2).execute()



