from peewee import *

my_db = MySQLDatabase(
    'vnexpress',
    host = 'localhost',
    user='root',
    password='123456'
)

class BaseModel(Model):

    class Meta:
        database = my_db

class City(BaseModel):
    id = PrimaryKeyField(null=False)
    name = CharField(max_length=35)
    countrycode = CharField(max_length=3)
    district = CharField(max_length=20)
    population = BigIntegerField()

City.create_table()
