import sys

from peewee import Model
from librarymanage.connection import library_mysql

class BaseModel(Model):
    class Meta:
        database = library_mysql