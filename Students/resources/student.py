import os
import json

from flask import request, jsonify, abort, make_response
from flask_restful import Resource, reqparse

from templates.models.student import info_student
#from template.config import *

class StudentResource(Resource):
    def get(self, id):
        s = info_student()
        try:
            res = s.get_by_id(id)
            if res:
                return jsonify(res)
            return make_response(jsonify({"message":"Student's not found"}), 404)
        except Exception as e:
            return make_response(jsonify({ "message": str(e) }), 400)