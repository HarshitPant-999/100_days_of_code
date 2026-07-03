from flask import Flask, render_template
from MyForm import MyForm


app = Flask(__name__)
app.config["SECRET_KEY"] = "serbia"

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()
    return render_template("login.html", form=form)



if __name__ == "__main__":
    app.run(debug=True)
