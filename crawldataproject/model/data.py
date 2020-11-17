from peewee import Model, CharField, IntegerField, DateTimeField, ForeignKeyField, BooleanField, TextField, JOIN, fn, FloatField,BigIntegerField
from crawldataproject.model import BaseModel
import requests

#create table
class Data(BaseModel):
    id = IntegerField(primary_key=True)
    name = CharField()
    productid = IntegerField()
    price = IntegerField()
    url = CharField()
    website = CharField()
    @classmethod
    def init_log(cls, **kwargs):
        return cls.insert(
            name=kwargs.get("name"),
            productid=kwargs.get("productid"),
            price=kwargs.get("price"),
            url=kwargs.get("url"),
            website=kwargs.get("website")
        ).execute()
    @classmethod
    def search(cls, id):
        data = cls.get(cls.id == id)
        return data.__dict__.get("__data__")
    @classmethod
    def search_list(cls):
        data = cls.select(cls.id, cls.name, cls.productid, cls.price, cls.url, cls.website).dicts()
        return [i for i in data]

    @classmethod
    def get_list_data(cls, **kwargs):
        h = cls.select(cls.id, cls.name, cls.productid, cls.price, cls.url, cls.website).dicts()
        keyword = kwargs.get("keyword")
        if keyword:
            a = h.where(cls.name.contains(keyword) | cls.productid.contains(keyword) | cls.website.contains(keyword))

            from_price = kwargs.get("from_price", 50000)
            b = a.where(cls.price >= from_price)

            to_price = kwargs.get("to_price", 100000)
            c = b.where(cls.price <= to_price)

            page_size = kwargs.get("page_size", 10)
            d = c.limit(int(page_size))

            page_index = kwargs.get("page_index", 0)
            data = d.offset(int(page_index))

            return [i for i in data]
