from flask import request, jsonify, abort, make_response
from flask_restful import Resource, reqparse

from librarymanage.models.borrowbook import Borrowbook


class InfoResource(Resource):
    def get(self):
        query = request.args
        try:
            res = Borrowbook.get_detail(query.get("id"))
            if res:
                return jsonify(res)
            return make_response(jsonify({"message": " Not Found"}), 404)
        except Exception as e:
            return make_response(jsonify({"message": str(e)}), 400)

    def post(self):
        query = request.get_json()
        try:
            id_ = Borrowbook.createInfo(**query)
            if id_:
                res = Borrowbook.get_detail(id_)
                return make_response(jsonify({"data": res}), 201)
            return make_response(jsonify({"message": "Book not found"}), 404)
        except Exception as e:
            return make_response(jsonify({"message": str(e)}), 400)

    def put(self):
        query = request.get_json()
        try:
            id_ = Borrowbook.updateInfo(**query)
            if id_:
                res = Borrowbook.get_detail(id_)
                return make_response(jsonify({"data": res}), 200)
            return make_response(jsonify({"message": "Not found to update"}), 404)
        except Exception as e:
            return make_response(jsonify({"message": "ok"}), 201)

    def delete(self):
        s = Borrowbook()
        query = request.args
        try:
            res = s.deleteInfo(query.get("id"))
            if res:
                return jsonify(res)
            return make_response(jsonify({"message": "OK"}), 200)
        except Exception as e:
            return make_response(jsonify({"message": str(e)}), 400)



