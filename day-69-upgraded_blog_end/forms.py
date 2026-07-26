from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

class RegisterForm(FlaskForm):
    name = StringField('name')
    email = StringField('email')
    password = PasswordField('password')
    submit = SubmitField("Submit")


class LoginForm(FlaskForm):
    name = StringField('name')
    email = StringField('email')
    password = PasswordField('password')
    submit = SubmitField("Submit")

# TODO: Create a CommentForm so users can leave comments below posts
