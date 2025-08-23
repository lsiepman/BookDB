from flask import render_template
from .functions import CreatorForm
from . import creators


@creators.route("/view_creators")
def view_creator_page():
    return render_template("view_creators.html")


@creators.route("/add_creator")
def add_creator_page():
    form = CreatorForm()
    if form.validate_on_submit():
        first_name = form.first_name
        family_name_prep = form.family_name_prep
        last_name = form.last_name

    return render_template("add_creator.html", form=form)
