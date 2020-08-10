from peewee import Model, CharField, IntegerField, DateTimeField, ForeignKeyField, BooleanField, TextField, JOIN, fn, DateField
from librarymanage.models import BaseModel
from librarymanage.models.book import Book
from librarymanage.models.user import  User
from flask import request

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
        cls.update(id_user=kwargs.get("id_user"),
                     id_book=kwargs.get("id_book"),
                     date=kwargs.get("date"),
                     price=kwargs.get("price")).where(cls.id ==12).execute()
       #return cls.get_detail()

    @classmethod
    def get_list(cls, keyword):
        # data3 = cls.select(cls.name, Score1.score, Subject.subject).join(Score1, on=(cls.id == Score1.id_student)).join(Subject, on=(
        # Subject.id == Score1.id_subject)).where(Score1.score <= to_score, Score1.score >= from_score).where(Student.id.contains(keyword)).dicts().limit(page_size).offset(page_index)

        #if keyword is None:
         #   return False
        #else:
        data = cls.select(cls.date, Book.name, User.name_user)\
            .join(User, on=(cls.id_user == User.id_user))\
            .join(Book, on=(cls.id_book == Book.id_book))\
            .where(User.name_user.contains(keyword)).dicts()
        page = request.args.get('page', 1, type=int)

        return [i for i in data.paginate(page, 5)]

"""
        if page_index is None:
            return False
        else:
            b = a.offset(page_index)

        if page_size is None:
            return False
        else:
            data3 = b.limit(page_size)
            return [i for i in data3]
"""








