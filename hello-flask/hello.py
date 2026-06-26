from flask import Flask

app = Flask(__name__)
print(__name__)

def make_bold(function):
    def wrapper():
       return f"<b>{function()}</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper

@app.route("/")
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
            '<p>This is a paragraph.</p>' \
            '<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%2Fid%2FOIP.5O3nwvf7dF88sz9x9uY5oAHaEK%3Fpid%3DApi&f=1&ipt=cad0bf38290d9eaf885ef6a2fec8a9b515c2ee6aa1eef7650efef7c5586f5b9c&ipo=images">'

@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def say_bye():
     return "Bye!"

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old!"

if __name__ == "__main__":
    app.run(debug=True)

