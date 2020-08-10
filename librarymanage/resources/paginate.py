from librarymanage.models.user import User
from flask import request, jsonify, abort, make_response
from flask_restful import Resource, reqparse
from flask import Flask, request, jsonify, abort
from flask_restful import Resource, Api
from librarymanage.models.borrowbook import Borrowbook

from datetime import datetime
from flask import render_template, flash, redirect, url_for, request



class BResource(Resource):
    def get(self):
        query = request.args
        #page = request.args.get('page', 1, type=int)
        #query1 = request.args.get("pagesize")
        #query2 = request.args.get("pageindex")
        try:
            res = Borrowbook.get_list(query.get("keyword"))
            if res:
                return jsonify(res)
            return make_response(jsonify({"message":"Info not found"}), 404)
        except Exception as e:
            return make_response(jsonify({ "message": str(e) }), 400)
