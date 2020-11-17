from flask import Flask
from crawldataproject.api1 import api_v1


def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret'
    return app

app = create_app()
api_v1.init_app(app)