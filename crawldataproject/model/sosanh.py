from peewee import Model, CharField, IntegerField, DateTimeField, ForeignKeyField, BooleanField, TextField, JOIN, fn, FloatField,BigIntegerField
from crawldataproject.model import BaseModel
from datetime import datetime


start = datetime.now()
#create table
class SoSanh(BaseModel):
    id = IntegerField(primary_key=True)
    time = DateTimeField()
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
    def search_min(cls):
        data = cls.select(cls.name ,cls.website ,cls.productid,cls.price,cls.time)\
            .where(cls.time == cls.select(fn.MAX(cls.time)))\
            .where(cls.price == cls.select(fn.MIN(cls.price))).limit(1).dicts()
        return [i for i in data]




