from flask import Flask


def create_app():
    app = Flask(__name__)

    from .creators import creators as creators_blueprint

    app.register_blueprint(creators_blueprint)

    return app
