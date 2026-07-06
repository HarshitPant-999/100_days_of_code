from flask import Flask, render_template, request, redirect, url_for
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)

all_books = []


@app.route('/')
def home():
    return render_template("index.html", book=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        Book_Name = request.form["book name"]
        Author_Name = request.form["book author"]
        Rating = request.form["rating"]
        return render_template("index.html", Book_Name=Book_Name, Author_Name=Author_Name, Rating=Rating)

    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)

