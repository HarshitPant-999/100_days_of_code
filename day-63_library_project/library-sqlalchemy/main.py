from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


db = SQLAlchemy()


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db.init_app(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=True, nullable=False)
    rating = db.Column(db.Float(10), nullable=False)

    def __repr__(self):
        return f"<Book {self.title}>"

with app.app_context():
    db.create_all() #CREATING THE TABLE
    new_book = Book(title="Sherlock Holmes", author="Sir Arthur Conan Doyle", rating=7.5)
    db.session.add(new_book)
    db.session.commit()
    result = db.session.execute(db.select(Book)).scalars().all()
    print(result)
    book = db.session.execute(db.select(Book).where(Book.title == "Sherlock Holmes")).scalar()
    print(book)
    book_to_update = db.session.execute(db.select(Book).where(Book.title == "Sherlock Holmes")).scalar()
    book_to_update.title = "Sherlock Holmes: A study in Scarlet"
    book_to_update.rating = 5.5
    db.session.commit()
    book_to_update = db.session.execute(db.select(Book).where(Book.id == 1)).scalar()
    book_to_update.title = "Sherlock Holmes: A hound of baskervilles"
    book_to_update.rating = 8.0
    db.session.commit()
    new_book = Book(title="Another Book", author="Some Author", rating=8.0)
    db.session.add(new_book)
    db.session.commit()
    book_to_delete = db.session.execute(db.select(Book).where(Book.id == 2)).scalar()
    db.session.delete(book_to_delete)
    db.session.commit()
