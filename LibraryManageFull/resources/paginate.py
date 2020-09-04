from librarymanage.models.user import User
from flask import request, jsonify, abort, make_response
from flask_restful import Resource, reqparse
from flask import Flask, request, jsonify, abort
from flask_restful import Resource, Api
from librarymanage.models.borrowbook import Borrowbook
from librarymanage.models.book import Book
from librarymanage.models.user import User

from datetime import datetime
from flask import render_template, flash, redirect, url_for, request



class BorrowFilterResource(Resource):
    def get(self):
        query = request.args
        try:
            res = Borrowbook.get_list(**query)
            if res:
                return jsonify(res)
            return make_response(jsonify({"message":"Info not found"}), 404)
        except Exception as e:
            return make_response(jsonify({ "message": str(e) }), 400)


class BookFilterResource(Resource):
    def get(self):
        query = request.args
        try:
            res = Book.get_list_book(**query)
            if res:
                return jsonify(res)
            return make_response(jsonify({"message":"Book not found"}), 404)
        except Exception as e:
            return make_response(jsonify({ "message": str(e) }), 400)

class UserFilterResource(Resource):
    def get(self):
        query = request.args
        try:
            res = User.get_list_user(**query)
            if res:
                return jsonify(res)
            return make_response(jsonify({"message":"User not found"}), 404)
        except Exception as e:
            return make_response(jsonify({ "message": str(e) }), 400)


