from flask import request, jsonify, abort, make_response
from flask_restful import Resource, reqparse
from crawldataproject.model.data import Data

class ListDataResource(Resource):
    def get(self):
        s = Data()
        try:
            res = s.search_list()
            if res:
                return jsonify(res)
            return make_response(jsonify({"message": "Not found"}), 404)
        except Exception as e:
            return make_response(jsonify({"message": str(e)}), 400)
class DataResource(Resource):
    def get(self):
        query = request.args
        try:
            res = Data.search(query.get("id"))
            if res:
                return jsonify(res)
            return make_response(jsonify({"message":"Not found"}), 404)
        except Exception as e:
            return make_response(jsonify({ "message": str(e) }), 400)

class DataFilterResource(Resource):
    def get(self):
        query = request.args
        try:
            res = Data.get_list_data(**query)
            if res:
                return jsonify(res)
            return make_response(jsonify({"message":"Not found"}), 404)
        except Exception as e:
            return make_response(jsonify({ "message": str(e) }), 400)
