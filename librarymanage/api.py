from flask_restful import Api , reqparse

from librarymanage.resources.user import UserResource
from librarymanage.resources.book import BookResource
from librarymanage.resources.borrowbook import InfoResource
from librarymanage.resources.ticket import Ticket
from librarymanage.resources.paginate import  BResource

api_v1 = Api()
api_v1.add_resource(UserResource, '/v1/users')
api_v1.add_resource(BookResource, '/v1/books' )
api_v1.add_resource(InfoResource, '/v1/borrows')
api_v1.add_resource(Ticket, '/v1/ticket/<id>')
api_v1.add_resource(BResource, '/v1/res')
