from flask import request, jsonify, abort, make_response
from flask_restful import Resource, reqparse

from librarymanage.models.user import User

class UserResource(Resource):
    def get(self):
        query = request.args
        try:
            res = User.search_by_id_user(query.get("id_user"))
            if res:
                return jsonify(res)
            return make_response(jsonify({"message": " Not Found"}), 404)
        except Exception as e:
            return make_response(jsonify({"message": str(e)}), 400)

    def post(self):
        query = request.get_json()
        try:
            id_ = User.createUser(**query)
            if id_:
                res = User.search_by_id_user(id_)
                return make_response(jsonify({"data": res}), 201)
            return make_response(jsonify({"message": "Book not found"}), 404)
        except Exception as e:
            return make_response(jsonify({"message": str(e)}), 400)

    def put(self):
        query = request.get_json()
        try:
            id_ = User.updateUser(**query)
            if id_:
                res = User.search_by_id_user(id_)
                return make_response(jsonify({"data": res}), 200)
            return make_response(jsonify({"message": "Not found to update"}), 404)
        except Exception as e:
            return make_response(jsonify({"message": "ok"}), 201)

    def delete(self):
        s = User()
        query = request.args
        try:
            res = s.deleteUser(query.get("id_user"))
            if res:
                return jsonify(res)
            return make_response(jsonify({"message": "OK"}), 200)
        except Exception as e:
            return make_response(jsonify({"message": str(e)}), 400)

