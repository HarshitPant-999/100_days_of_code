from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import csv
import requests
import os

api_key = os.environ.get("TMDB_API_KEY")
db = SQLAlchemy()

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie_list.db"
db.init_app(app)

class MovieForm(FlaskForm):
    title = StringField("Movie Title")
    submit = SubmitField("submit")


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=False, nullable=False)
    year = db.Column(db.String(250), unique=False, nullable=False)
    description = db.Column(db.String(2500), nullable=False)
    rating = db.Column(db.Float(250), nullable=True)
    ranking = db.Column(db.Float(250), nullable=True)
    review = db.Column(db.String(2500), nullable=True)
    img_url = db.Column(db.String(10), nullable=False)
    

class RateMovieForm(FlaskForm):
    rating = StringField("rating")
    review = StringField("review")
    submit = SubmitField("submit")

#with app.app_context():
#    db.create_all()
#    new_movie = Movie(
#        title="Phone Booth",
#        year=2002,
#        description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#        rating=7.3,
#        ranking=10,
#        review="My favourite character was the caller.",
#        img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
#    )
#    db.session.add(new_movie)
#    db.session.commit()

@app.route("/")
def home():
    all_movies = db.session.execute(db.select(Movie).order_by(Movie.rating)).scalars().all()
    return render_template("index.html", movies=all_movies)

@app.route("/add", methods=["POST", "GET"])
def add():
    form = MovieForm()
    if form.validate_on_submit():
        response = requests.get(url="https://api.themoviedb.org/3/search/movie", params={"query":form.title.data, "api_key":api_key, "include_adult":"True", "language":"en-US"})
        data = response.json()
        new_movie = Movie(
            title = data["results"][0]["title"],
            year = data["results"][0]["release_date"],
            description = data["results"][0]["overview"],
            ranking = 0,
            rating = 0,
            review = 0,
            img_url = data["results"][0]["poster_path"]
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html", form=form)

@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = RateMovieForm()
    if form.validate_on_submit():
        movie_id = request.args.get("id")
        movie_to_update = db.get_or_404(Movie, movie_id)
        movie_to_update.rating = form.rating.data
        movie_to_update.review = form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    movie_id = request.args.get("id")
    movie_to_update = db.get_or_404(Movie, movie_id)
    return render_template("edit.html", form=form)

@app.route("/delete")
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
