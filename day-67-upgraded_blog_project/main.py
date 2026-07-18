from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import datetime

class PostForm(FlaskForm):
    title = StringField('Blog Post Title')
    subtitle = StringField('Subtitle')
    body = CKEditorField('Body')
    author = StringField('Your Name')
    img_url = StringField('Blog Image URL')
    submit = SubmitField('Submit')

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
ckeditor = CKEditor(app)

class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

date = datetime.now()
today_date = date.date()

class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    all_blogs = db.session.execute(db.select(BlogPost)).scalars().all()
    posts = all_blogs
    return render_template("index.html", all_posts=posts)


@app.route('/<int:post_id>', methods=["GET", "POST"])
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)

@app.route("/new-post", methods=["GET", "POST"])
def add_new_post():
    form = PostForm()
    if request.method == "POST":
        new_blog = BlogPost(
        title = form.title.data,
        subtitle = form.subtitle.data,
        date = today_date,
        body = form.body.data,
        author = form.author.data,
        img_url = form.img_url.data)
        db.session.add(new_blog)
        db.session.commit()
        return redirect (url_for("get_all_posts"))
    return render_template("make-post.html", form=form, is_edit=False)

@app.route("/edit-post/<post_id>" , methods=["GET", "POST"])
def edit_post(post_id):
    form = PostForm()
    post = db.get_or_404(BlogPost, post_id)
    if request.method == "GET":
        edit_form = PostForm(
            title=post.title,
            subtitle=post.subtitle,
            img_url=post.img_url,
            author=post.author,
            body=post.body
        )
        return render_template("make-post.html", form=edit_form, is_edit=True)
    if request.method == "POST":
        post.title = form.title.data
        post.subtitle = form.subtitle.data
        post.body = form.body.data
        post.author = form.author.data
        post.img_url = form.img_url.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))


@app.route("/delete/<post_id>")
def delete_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('get_all_posts'))

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
