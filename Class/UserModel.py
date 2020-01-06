from flask import request
from model import mysql
class UserModel:
    def post():
        user = request.form
        name = user['name']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO vnexpress.list(name) VALUES(%s)",[name])
        mysql.connection.commit()