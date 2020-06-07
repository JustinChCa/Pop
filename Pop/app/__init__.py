from flask import Flask, url_for


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config['SECRET_KEY'] = 'dev'

    with app.app_context():
        from .bp import bp

        app.register_blueprint(bp, url_prefix="/")

    return app
