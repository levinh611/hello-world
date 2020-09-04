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
                          author = kwargs.get("author")).where(cls.id_book==9).execute()


    @classmethod
    def get_list_book(cls, **kwargs):
        h = cls.select(cls.id_book, cls.name, cls.types, cls.publisher ,cls.author).dicts()
        keyword = kwargs.get("keyword")
        if keyword:
            a = h.where(Book.name.contains(keyword) | Book.types.contains(keyword))

        page_size = kwargs.get("page_size", 5)
        b = a.limit(int(page_size))

        page_index = kwargs.get("page_index", 0)
        c = b.offset(int(page_index))

        from_publisher = kwargs.get("from_publisher", 2019)
        d = c.where(cls.publisher >= from_publisher)

        to_publisher = kwargs.get("to_publisher", 2020)
        e = d.where(cls.publisher <= to_publisher)

        order_field = kwargs.get("order_field", "name")
        data = e.order_by(getattr(cls, order_field).asc())
        return [i for i in data]

