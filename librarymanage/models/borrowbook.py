from peewee import Model, CharField, IntegerField, DateTimeField, ForeignKeyField, BooleanField, TextField, JOIN, fn, DateField
from librarymanage.models import BaseModel
from librarymanage.models.book import Book
from librarymanage.models.user import  User

class Borrowbook(BaseModel):
    id = IntegerField(primary_key=True)
    id_user = IntegerField()
    id_book = IntegerField()
    date = DateField()
    price = IntegerField()

    @classmethod
    def init_log(cls, **kwargs):
        return cls.insert(
            id_user=kwargs.get("id_user"),
            id_book=kwargs.get("id_book"),
            date=kwargs.get("date"),
            price=kwargs.get("price")
        ).execute()

    @classmethod
    def get_detail(cls, id):
        data = cls.get(cls.id == id)
        return data.__dict__.get("__data__")

    @classmethod
    def search(cls, id):
        data = cls.select(cls.date, Book.name, User.name_user, cls.price) \
            .join(User, on=(cls.id_user == User.id_user)) \
            .join(Book, on=(cls.id_book == Book.id_book)) \
            .where(cls.id == id).dicts()
        return [i for i in data]

    @classmethod
    def createInfo(cls, **kwargs):
        return cls.insert(id=kwargs.get("id"),
                          id_user=kwargs.get("id_user"),
                          id_book=kwargs.get("id_book"),
                          date=kwargs.get("date"),
                          price=kwargs.get("price")).execute()

    @classmethod
    def deleteInfo(cls, id):
        a = cls.delete().where(cls.id == id)
        a.execute()

    @classmethod
    def updateInfo(cls, **kwargs):
        cls.update(id=kwargs.get("id"),
                          id_user=kwargs.get("id_user"),
                          id_book=kwargs.get("id_book"),
                          date=kwargs.get("date"),
                          price=kwargs.get("price")).where(cls.id ==6).execute()
        return cls.get_detail()

