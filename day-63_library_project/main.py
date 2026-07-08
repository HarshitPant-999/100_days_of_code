from flask import Flask, render_template, request, redirect, url_for
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import csv

db = SQLAlchemy()

app = Flask(__name__)
app.secret_key = "your-secret-key-here"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db.init_app(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=False, nullable=False)
    rating = db.Column(db.Float(10), nullable=False)

with app.app_context():
    db.create_all() #CREATING THE TABLE


class BookForm(FlaskForm):
    title = StringField("book name")
    author = StringField("book author")
    rating = StringField("rating")

class ChangeRatingForm(FlaskForm):
    rating = StringField("rating")

@app.route('/')
def home():
    all_books = db.session.execute(db.select(Book)).scalars().all()
    return render_template("index.html", all_books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = BookForm()
    if form.validate_on_submit():
        new_book = Book(
            title=form.title.data,
            author=form.author.data,
            rating=float(form.rating.data)
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html", form=form)

@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        book_id = request.form["id"]
        book_to_update = db.get_or_404(Book, book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for("home"))
    book_id = request.args.get('id')
    book_selected = db.get_or_404(Book, book_id) #WHAT'S get_or_404 
    return render_template("edit.html", book=book_selected)

@app.route("/delete")
def Delete():
    book_id = request.args.get('id')
    book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

