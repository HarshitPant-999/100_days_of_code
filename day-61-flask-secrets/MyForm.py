from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Regexp , Length

class MyForm(FlaskForm):
    email = StringField("Email", validators=[Regexp(r'^[^@]+@[^@]+\.[^@]+$', message="Please enter a valid email address.!")])
    password = PasswordField("Password", validators=[Length(min=8, message="password must be of at least 8 characters")])
    submit = SubmitField("Log in")
