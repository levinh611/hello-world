import peewee
from peewee import Model , CharField , IntegerField
from flask import request, jsonify, abort, make_response, Flask
from flask_restful import Resource, reqparse, Api


mysql = peewee.MySQLDatabase("vnexpress",host="localhost",port=3306,user="root",passwd="123456")
class BaseModel(Model):
    class Meta:
        database = mysql

class club1(BaseModel):
    id = IntegerField(primary_key=True)
    name = CharField()
    manager = CharField()

    @classmethod
    def init_log(cls, **kwargs):
        return cls.insert(
            name=kwargs.get("name"),
            manager=kwargs.get("manager")
        ).execute()

    @classmethod
    def get_by_id(cls, id):
        return cls.get(cls.id == id)


class ClubResource(Resource):
    def get(self, id):
        s = club1()
        try:
            res = s.get_by_id(id)
            if res:
                return jsonify(res)
            return make_response(jsonify({"message":"Club not found"}), 404)
        except Exception as e:
            return make_response(jsonify({ "message": e }), 400)

api_v1 = Api()
api_v1.add_resource(ClubResource, '/info/<id>')

def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret'
    return app

app = create_app()
api_v1.init_app(app)


app.run()



















