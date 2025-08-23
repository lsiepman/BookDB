from flask import Blueprint

creators = Blueprint(
    "creators", __name__, template_folder="templates", static_folder="static"
)

from . import routes
