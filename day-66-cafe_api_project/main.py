from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random

app = Flask(__name__)

class Base(DeclarativeBase):
    pass

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=True)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=True)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=True)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return {
        "name": self.name,
        "map_url": self.map_url,
        "img_url": self.img_url,
        "location": self.location,
        "seats": self.seats,
        "has_toilet": self.has_toilet,
        "has_wifi": self.has_wifi,
        "has_sockets": self.has_sockets,
        "can_take_calls": self.can_take_calls,
        "coffee_price": self.coffee_price
        }



with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random", methods=["POST", "GET"])
def get_random_cafe():
    all_cafes = db.session.execute(db.select(Cafe)).scalars().all()
    random_cafe = random.choice(all_cafes)
    return jsonify(cafe =
        random_cafe.to_dict()
    )

@app.route("/all")
def all():
    all_cafes = db.session.execute(db.select(Cafe)).scalars().all()
    return jsonify(cafes = [cafe.to_dict() for cafe in all_cafes])

@app.route("/search")
def search():
    cafe_location = request.args.get("loc")
    all_cafes = db.session.execute(db.select(Cafe).where(Cafe.location == cafe_location)).scalars().all()
    if all_cafes:
        return jsonify(cafes = [cafe.to_dict() for cafe in all_cafes])
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404

@app.route("/get", methods=["GET", "POST"])
def get_new_cafe():
    if request.method == "POST":
        cafe = Cafe(
            name = request.form.get("name"),
            map_url = request.form.get("map_url"),
            img_url = request.form.get("img_url"),
            location = request.form.get("location"),
            seats = request.form.get("seats"),
            has_toilet = request.form.get("has_toilet") == "true",
            has_wifi = request.form.get("has_wifi") == "true",
            has_sockets = request.form.get("has_sockets") == "true",
            can_take_calls = request.form.get("can_take_calls") == "true",
            coffee_price = request.form.get("coffee_price"))
        db.session.add(cafe)
        db.session.commit()
        return jsonify(response={"success": "Successfully added the new cafe."})
# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
