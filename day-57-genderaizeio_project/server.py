from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/guess/<name>")
def guess(name):
    response = requests.get("https://api.genderize.io", params={"name":"harshit"})
    data = response.json()
    possible_gender = data["gender"]
    response = requests.get("https://api.agify.io", params={"name":"harshit"})
    year = response.json()
    possible_age = year["age"]
    return render_template("index.html", gen=possible_gender, age=possible_age, name=name)

if __name__ == "__main__":
    app.run(debug=True)


