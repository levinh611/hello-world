import peewee
from peewee import Model , CharField , IntegerField
from flask import request, jsonify, abort, make_response, Flask
from flask_restful import Resource, reqparse, Api


mysql = peewee.MySQLDatabase("vnexpress",host="localhost",port=3306,user="root",passwd="123456")
class BaseModel(peewee.Model):
    class Meta:
        database = mysql

class club1(BaseModel):
    id = peewee.IntegerField(primary_key=True)
    name = peewee.CharField()
    manager = peewee.CharField()

    @classmethod
    def init_log(cls, **kwargs):
        return cls.insert(
            name=kwargs.get("name"),
            manager=kwargs.get("manager")
        ).execute()

    @classmethod
    def get_by_id(cls, id):
        #data = cls.select().where(cls.id == id).dicts()
        #return [i for i in data]\
        #import ipdb;ipdb.set_trace()
        data = cls.get(cls.id==id)
        return data.__dict__.get("__data__")


class ClubResource(Resource):
    def get(self, id):
        s = club1()
        try:
            res = s.get_by_id(id)
            if res:
                return jsonify(res)
            return make_response(jsonify({"message":"Club not found"}), 404)
        except Exception as e:
            return make_response(jsonify({ "message": str(e) }), 400)


class ClubList(Resource):
    def get(self):
        return club1


api_v1 = Api()
api_v1.add_resource(ClubList, '/info')
api_v1.add_resource(ClubResource, '/info1/<id>/')

def create_app() -> Flask:
    print("hello")

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret'
    return app

app = create_app()
api_v1.init_app(app)

if __name__=='__main__':
    app.run(debug=True)





