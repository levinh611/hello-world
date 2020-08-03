from flask import request, jsonify, abort, make_response
from flask_restful import Resource, reqparse

from librarymanage.models.borrowbook import Borrowbook


class Ticket(Resource):
    def get(self, id):
        s = Borrowbook()
        try:
            res = Borrowbook.search(id)
            if res:
                return jsonify(res)
            return make_response(jsonify({"message": "Ticket not found"}), 404)
        except Exception as e:
            return make_response(jsonify({"message": str(e)}), 400)