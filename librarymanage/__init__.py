from flask import Flask
from librarymanage.api import api_v1

#from Student.config import *

def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret'
    return app

app = create_app()
api_v1.init_app(app)