import peewee

ex_mysql = peewee.MySQLDatabase(
        "vnexpress",
        host="localhost",
        port=3306,
        user="root",
        passwd="123456",
        )