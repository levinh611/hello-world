from librarymanage import app
from librarymanage.documents import swaggerui_blueprint

app.register_blueprint(swaggerui_blueprint)


if __name__=='__main__':
        app.run(debug=True)

