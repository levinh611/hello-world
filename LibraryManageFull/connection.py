import peewee

library_mysql = peewee.MySQLDatabase(
        "library manage",
        host="localhost",
        port=3306,
        user="root",
        passwd="123456")