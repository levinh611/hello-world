from peewee import Model, CharField, IntegerField, DateTimeField, ForeignKeyField, BooleanField, TextField, JOIN, fn

from templates.models import BaseModel

class info_student(BaseModel):
    id = IntegerField(primary_key=True)
    name = CharField()
    gender = CharField()

    @classmethod
    def init_log(cls, **kwargs):
        return cls.insert(
                name=kwargs.get("name"),
                gender=kwargs.get("gender"),
                ).execute()

    @classmethod
    def get_by_id(cls, id):
        data = cls.get(cls.id == id)
        return data.__dict__.get("__data__")