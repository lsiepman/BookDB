from flask import render_template
from .functions import AuthorForm
from . import authors


@authors.route("/view_authors")
def view_author_page():
    return render_template("view_authors.html")


@authors.route("/add_author")
def add_author_page():
    form = AuthorForm()
    if form.validate_on_submit():
        first_name = form.first_name
        family_name_prep = form.family_name_prep
        last_name = form.last_name

    return render_template("add_author.html", form=form)
