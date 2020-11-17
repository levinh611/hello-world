from flask import request, jsonify, abort, make_response
from flask_restful import Resource, reqparse
from crawldataproject.model.input import Input

class InputResource(Resource):
    def get(self):
        s = Input()
        try:
            res = s.search()
            if res:
                return jsonify(res)
            return make_response(jsonify({"message": "Not found"}), 404)
        except Exception as e:
            return make_response(jsonify({"message": str(e)}), 400)
class InputFilterResource(Resource):
    def get(self):
        query = request.args
        try:
            res = Input.get_list_input(**query)
            if res:
                return jsonify(res)
            return make_response(jsonify({"message":"Not found"}), 404)
        except Exception as e:
            return make_response(jsonify({ "message": str(e) }), 400)