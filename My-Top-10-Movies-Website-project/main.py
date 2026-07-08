from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import csv

db = SQLAlchemy()

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie_list.db"
db.init_app(app)

class MovieForm(FlaskForm):
    title = StringField("title")
    year = StringField("year")
    description = StringField("Description")
    rating = StringField("rating")
    ranking = StringField("ranking")
    review = StringField("review")
    img_url = StringField("img_url")
    submit = StringField("submit")


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=False, nullable=False)
    year = db.Column(db.String(250), unique=False, nullable=False)
    description = db.Column(db.String(2500), nullable=False)
    rating = db.Column(db.Float(10), nullable=False)
    ranking = db.Column(db.Float(250), nullable=False)
    review = db.Column(db.String(10), nullable=False)
    img_url = db.Column(db.String(10), nullable=False)


with app.app_context():
    db.create_all()
    new_movie = Movie(
        title="Phone Booth",
        year=2002,
        description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
        rating=7.3,
        ranking=10,
        review="My favourite character was the caller.",
        img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
    )
    db.session.add(new_movie)
    db.session.commit()

@app.route("/")
def home():
    all_movies = db.session.execute(db.select(Movie)).scalars().all()
    return render_template("index.html", movies=all_movies)

def add():
    form = MovieForm()
    if form.validate_on_submit():
        new_movie = Movie(
            title=form.title.data,
            year=form.year.data,
            description=form.description.data,
            rating=form.rating.data,
            ranking=form.ranking.data,
            review=form.review.data,
            img_url=form.img_url.data
        )
        db.session.add(new_movie)
        db.session.commit()
    render_template("add.html")

if __name__ == '__main__':
    app.run(debug=True)
