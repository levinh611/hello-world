import sys

from peewee import Model
from crawldataproject.connection import ex_mysql

class BaseModel(Model):
    class Meta:
        database = ex_mysql