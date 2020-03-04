import peewee as pw
my_db = pw.MySQLDatabase('vnexpress', user = 'root', passwd ='123456',host = 'localhost')
class Student(pw.Model):
    class Meta:
        database = my_db
class Info611(Student):
    id = pw.IntegerField()
    full_name = pw.CharField()
    MSSV = pw.IntegerField()
    age = pw.IntegerField()

Info611.create(id = '3', full_name = 'Lê Vinh', MSSV ='1234', age = '18')



