from flask_wtf import FlaskForm
from wtforms import StringField, DateField, BooleanField, SubmitField
from wtforms.validators import InputRequired


class CreatorForm(FlaskForm):
    first_name = StringField("First name", validators=[InputRequired()])
    family_name_prep = StringField("Infix")
    last_name = StringField("Last name", validators=[InputRequired()])
    nationality = StringField("Nationality")
    dob = DateField("Date of birth")
    pseudonym = BooleanField("Name is pseudonym")
    real_first_name = StringField("First name")
    real_family_name_prep = StringField("Infix")
    real_last_name = StringField("Last name")
    submit = SubmitField("Submit")
