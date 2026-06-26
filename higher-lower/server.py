from flask import Flask
import random
number = random.randint(0, 10)


app = Flask(__name__)

@app.route("/")
def home():
    return '<h1>"Guess a number between 0 and 9"</h1>' \
            '<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExZjlyNWliZDlxcWx1Y3NkNDZ1emsxbXI1bzdvZ3Q3ZzZ0bjJrcW41dCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/10Jpr9KSaXLchW/giphy.gif"/>'

@app.route("/<int:guess>")
def guess_number(guess):
    if guess > number:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"

    elif guess < number:
        return "<h1 style='color: red'>Too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"

    else:
        return "<h1 style='color: green'>You found it!</h1>" \
                "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"

if __name__ == "__main__":
    app.run(debug=True)
