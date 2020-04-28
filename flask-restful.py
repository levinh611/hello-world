from flask import Flask
from flask_restful import Api , Resource , abort

app = Flask(__name__)
api = Api(app)


Club = {
    'club1':{'club':'FC Barcelona',
             'manager':'Quique Setien'},
    'club2':{'club':'Real Madrid',
             'manager':'Zinedine Zidane'},
    'club3':{'club':'Chelsea',
             'manager':'Frank Lampard'},
    'club4':{'club':'Liverpool',
             'manager':'Jurgen Klopp'},
    'club5':{'club':'Juventus',
             'manager':'Maurizio Sarri'}
}
def Error(club_id):
    if club_id not in Club:
        abort(404, message = 'No Result')





class club(Resource):
    def get(self, club_id):
        Error(club_id)
        return Club[club_id]

    def delete(self, club_id):
        Error(club_id)
        del Club[club_id]
        return '', 204

    def put(self, club_id):
        pass


class ClubList(Resource):
    def get(self):
        return Club



api.add_resource(ClubList, '/club')
api.add_resource(club, '/club/<club_id>')

if __name__ == '__main__':
    app.run(debug=True)





