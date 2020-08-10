from flask import request, jsonify, abort, make_response
from flask_restful import Resource, reqparse, request

from librarymanage.models.book import Book

class BookResource(Resource):
    def get(self):
        query = request.args
        try:
            res = Book.search_by_id_book(query.get("id_book"))
            if res:
                return jsonify(res)
            return make_response(jsonify({"message":"Book not found"}), 404)
        except Exception as e:
            return make_response(jsonify({ "message": str(e) }), 400)

    def post(self):
        query = request.get_json()
        try:
            id_ = Book.createBook(**query)
            if id_:
                res = Book.search_by_id_book(id_)
                return make_response(jsonify({"data":res}), 201)
            return make_response(jsonify({"message": "Book not found"}), 404)
        except Exception as e:
            return make_response(jsonify({"message": str(e)}), 400)

    def put(self):
        query = request.get_json()
        try:
            id_ = Book.updateBook(**query)
            if id_:
                res = Book.search_by_id_book(id_)
                return make_response(jsonify({"data":res}), 201)
            return make_response(jsonify({"message": "ok"}), 200)
        except Exception as e:
            return make_response(jsonify({"message": str(e)}), 201)
    #def put(self):
        #query = request.args
     #  try:
         #   res = Book.search_by_id_book(query.get("id_book"))
          #  if res:
           #     return jsonify(res)
           # return make_response(jsonify({"message": "Book not found"}), 404)
        #except Exception as e:
         #   return make_response(jsonify({"message": str(e)}), 400)


    def delete(self):
        s = Book()
        query = request.args
        try:
            res = s.deleteBook(query.get("id_book"))
            if res:
                return jsonify(res)
            return make_response(jsonify({"message":"OK"}), 200)
        except Exception as e:
            return make_response(jsonify({ "message": str(e) }), 400)




