from flask import Blueprint

authors = Blueprint(
    "authors", __name__, template_folder="templates", static_folder="static"
)

from . import routes
