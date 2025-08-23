import json
from flask import Flask, render_template
from .general_functions import fetch_secret_key
from . import create_app

app = create_app()
app.config["SECRET_KEY"] = fetch_secret_key()


@app.route("/favicon.ico")
def favicon():
    return "", 204  # No Content


@app.route("/")
def home():
    return render_template("home.html")
