from flask_restful import Api , reqparse
from crawldataproject.resources.sosanh import SoSanhResource
from crawldataproject.resources.input import InputResource, InputFilterResource
from crawldataproject.resources.data import DataResource, ListDataResource, DataFilterResource

api_v1 = Api()
api_v1.add_resource(InputResource, '/v1/input')
api_v1.add_resource(SoSanhResource, '/v1/sosanh')
api_v1.add_resource(ListDataResource, '/v1/datalist')
api_v1.add_resource(DataResource, '/v1/data')
api_v1.add_resource(DataFilterResource, '/v1/datafilter')
api_v1.add_resource(InputFilterResource, '/v1/inputfilter')
