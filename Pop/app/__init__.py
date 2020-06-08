from flask import Flask
from flask_socketio import SocketIO

socket = SocketIO()


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config['SECRET_KEY'] = 'dev'
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

    with app.app_context():
        from .listen.routes import routes
        from .listen import events

        app.register_blueprint(routes, url_prefix="/")
        socket.init_app(app)

    return app
