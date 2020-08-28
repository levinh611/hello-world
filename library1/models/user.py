from peewee import Model, CharField, IntegerField, DateTimeField, ForeignKeyField, BooleanField, TextField, JOIN, fn, FloatField

from librarymanage.models import BaseModel
from flask import Flask, request, jsonify, abort
from flask_restful import Resource, Api



class User(BaseModel):
    id_user = IntegerField(primary_key=True)
    name_user = CharField()
    age = IntegerField()
    address = CharField()
    phone = CharField()

    @classmethod
    def init_log(cls, **kwargs):
        return cls.insert(
            name_user=kwargs.get("name_user"),
            age = kwargs.get("age"),
            address=kwargs.get("address"),
            phone=kwargs.get("phone")).execute()

    @classmethod
    def search_by_id_user(cls, id_user):
        data = cls.get(cls.id_user == id_user)
        return data.__dict__.get("__data__")

    @classmethod
    def createUser(cls, **kwargs):
        return cls.insert(id_user = kwargs.get("id_user"),
                          name_user = kwargs.get("name_user"),
                          age = kwargs.get("age"),
                          address = kwargs.get("address"),
                          phone = kwargs.get("phone")).execute()


    @classmethod
    def updateUser(cls, **kwargs):
        cls.update(id_user = kwargs.get("id_user"),
                          name_user = kwargs.get("name_user"),
                          age = kwargs.get("age"),
                          address = kwargs.get("address"),
                          phone = kwargs.get("phone")).where(cls.id_user == 5).execute()

    @classmethod
    def deleteUser(cls, id_user):
        n = cls.delete().where(cls.id_user == id_user)
        n.execute()


    @classmethod
    def get_list_user(cls, **kwargs):
        h = cls.select(cls.id_user, cls.name_user, cls.age, cls.address, cls.phone).dicts()
        keyword = kwargs.get("keyword")
        if keyword:
            a = h.where(User.name_user.contains(keyword) | User.age.contains(keyword))

        page_size = kwargs.get("page_size", 5)
        b = a.limit(int(page_size))

        page_index = kwargs.get("page_index", 0)
        c = b.offset(int(page_index))

        from_age = kwargs.get("from_age", 10)
        d = c.where(cls.age >= from_age)

        to_age = kwargs.get("to_age"), 20
        e = d.where(cls.age <= to_age)

        order_field = kwargs.get("order_field", "age")
        data = e.order_by(getattr(cls, order_field).asc())
        return [i for i in data]


