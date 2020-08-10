from peewee import Model, CharField, IntegerField, DateTimeField, ForeignKeyField, BooleanField, TextField, JOIN, fn, FloatField
from librarymanage.models import BaseModel
from flask_restful import abort

class Book(BaseModel):
    id_book = IntegerField(primary_key=True)
    name = CharField()
    types = CharField()
    publisher = CharField()
    language = CharField()
    author = CharField()

    @classmethod
    def init_log(cls, **kwargs):
        return cls.insert(
            name=kwargs.get("name"),
            types=kwargs.get("types"),
            publisher=kwargs.get("publisher"),
            language=kwargs.get("language"),
            author = kwargs.get("author")
        ).execute()

    @classmethod
    def search_by_id_book(cls, id_book):
        data = cls.get(cls.id_book == id_book)
        return data.__dict__.get("__data__")

    @classmethod
    def createBook(cls, **kwargs):
        return cls.insert(
                          name=kwargs.get("name"),
                          types=kwargs.get("types"),
                          publisher=kwargs.get("publisher"),
                          language=kwargs.get("language"),
                          author = kwargs.get("author")).execute()

    @classmethod
    def deleteBook(cls, id_book):
        a = cls.delete().where(cls.id_book == id_book)
        a.execute()

    @classmethod
    def updateBook(cls, **kwargs):
        cls.update(
                          name=kwargs.get("name"),
                          types=kwargs.get("types"),
                          publisher=kwargs.get("publisher"),
                          language=kwargs.get("language"),
                          author = kwargs.get("author")).execute()
        return cls.search_by_id_book(cls.id_book==Book.id_book)
