from flask_restful import Api

from templates.resources.student import StudentResource

api_v1 = Api()
api_v1.add_resource(StudentResource, '/student/<id>')