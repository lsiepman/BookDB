from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired


class AuthorForm(FlaskForm):
    first_name = StringField("First name", validators=[InputRequired()])
    family_name_prep = StringField("Family name preposition")
    last_name = StringField("Last name", validators=[InputRequired()])
