from peewee import Model, CharField, IntegerField, DateTimeField, ForeignKeyField, BooleanField, TextField, JOIN, fn, DateField
from librarymanage.models import BaseModel
from librarymanage.models.book import Book
from librarymanage.models.user import  User
from flask import request
#from librarymanage.models.test import TestUpdate
import unittest



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


   # @classmethod
   ##    # data3 = cls.select(cls.name, Score1.score, Subject.subject).join(Score1, on=(cls.id == Score1.id_student)).join(Subject, on=(
        # Subject.id == Score1.id_subject)).where(Score1.score <= to_score, Score1.score >= from_score).where(Student.id.contains(keyword)).dicts().limit(page_size).offset(page_index)

        #if keyword is None:
         #   return False
        #else:
     #   data1 = cls.select(cls.date, Book.name, User.name_user, User.age)\
      #      .join(User, on=(cls.id_user == User.id_user))\
       #     .join(Book, on=(cls.id_book == Book.id_book))\
        #    .where(User.name_user.contains(kwargs["keyword"]) | Book.name.contains(kwargs["keyword"]))\
         #   .dicts()
        #if kwargs['to_age']:
         #   data = data1.where(User.age <= kwargs['to_age'])


        #page = request.args.get('page', 1, type=int)
        #return [i for i in data1.paginate(page, 5)]
        #return [i for i in data1]

        
    @classmethod
    def get_list(cls, **kwargs):
        h = cls.select(cls.date ,User.name_user, Book.name,User.age, cls.price) \
            .join(User, on=(cls.id_user == User.id_user)) \
            .join(Book, on=(cls.id_book == Book.id_book)).dicts()

        keyword = kwargs.get("keyword")
        if keyword:
            a= h.where(User.name_user.contains(keyword) | Book.name.contains(keyword) | User.age.contains(keyword) |
            User.address.contains(keyword))

        page_size =  kwargs.get("page_size", 5)
        b = a.limit(int(page_size))

        page_index = kwargs.get("page_index", 0)
        c = b.offset(int(page_index))

        from_date = kwargs.get("from_date", "2019-01-13")
        d = c.where(cls.date >= from_date)
        to_date =  kwargs.get("to_date", "2019-12-07")
        e = d.where(cls.date <= to_date)

        from_price = kwargs.get("from_price", 2000)
        f = e.where(cls.price >= from_price)
        to_price = kwargs.get("to_price", 100000)
        g = f.where(cls.price <= to_price)

        order_field = kwargs.get("order_field", "id")
        data = g.order_by(getattr(cls, order_field).asc())
        return [i for i in data]




    
    """
        @classmethod
        def get_list(cls, keyword, page_index, page_size, from_date, to_date, from_price, to_price,  order_field):
            data = cls.select(cls.date, User.name_user, Book.name, cls.price)\
            .join(User, on=(cls.id_user == User.id_user))\
            .join(Book, on=(cls.id_book == Book.id_book))\
            .where(User.name_user.contains(keyword) | Book.name.contains(keyword))\
            .dicts().limit(page_size).offset(page_index)\
            .where(cls.date >= from_date & cls.date <= to_date)\
            .where(cls.price >= from_price & cls.price <= to_price)\
            .order_by(order_field.desc())
            print(max(User.age))
    """























