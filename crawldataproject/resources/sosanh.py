from flask import request, jsonify, abort, make_response
from flask_restful import Resource, reqparse
from crawldataproject.model.sosanh import SoSanh

class SoSanhResource(Resource):
    def get(self):
        s = SoSanh()
        try:
            res = s.search_min()
            if res:
                return jsonify(res)
            return make_response(jsonify({"message": "Not found"}), 404)
        except Exception as e:
            return make_response(jsonify({"message": str(e)}), 400)
