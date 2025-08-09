import json
from flask import Flask, render_template
from .general_functions import fetch_secret_key
from .authors.routes import authors


app = Flask(__name__)
app.config["SECRET_KEY"] = fetch_secret_key()

# register all blueprints
app.register_blueprint(authors)


@app.route("/favicon.ico")
def favicon():
    return "", 204  # No Content


@app.route("/")
def home():
    return render_template("home.html")
