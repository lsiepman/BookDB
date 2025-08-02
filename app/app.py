import json
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired
from .general_functions import fetch_secret_key


class AuthorForm(FlaskForm):
    first_name = StringField("First name", validators=[InputRequired()])
    family_name_prep = StringField("Family name preposition")
    last_name = StringField("Last name", validators=[InputRequired()])


app = Flask(__name__)
app.config["SECRET_KEY"] = fetch_secret_key()


@app.route("/favicon.ico")
def favicon():
    return "", 204  # No Content


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/view_authors")
def view_author_page():
    return render_template("view_authors.html")


@app.route("/add_author")
def add_author_page():
    form = AuthorForm()
    if form.validate_on_submit():
        first_name = form.first_name
        family_name_prep = form.family_name_prep
        last_name = form.last_name

    return render_template("add_author.html", form=form)
