from peewee import Model, CharField, IntegerField, DateTimeField, ForeignKeyField, BooleanField, TextField, JOIN, fn, FloatField

from librarymanage.models import BaseModel



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
        return cls.update(id_user = kwargs.get("id_user"),
                          name_user = kwargs.get("name_user"),
                          age = kwargs.get("age"),
                          address = kwargs.get("address"),
                          phone = kwargs.get("phone")).where(cls.id_user == 6).execute()
    @classmethod
    def deleteUser(cls, id_user):
        n = cls.delete().where(cls.id_user == id_user)
        n.execute()




