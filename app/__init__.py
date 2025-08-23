from flask import Flask


def create_app():
    app = Flask(__name__)

    from .authors import authors as authors_blueprint

    app.register_blueprint(authors_blueprint)

    return app
