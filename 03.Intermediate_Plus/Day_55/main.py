from flask import Flask

def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper

def make_emph(function):
    def wrapper():
        return f"<emp>{function()}</emp>"
    return wrapper

def make_itallics(function):
    def wrapper():
        return f"<i>{function()}</i>"
    return wrapper

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World</h1>' \
        '<p>This is a paragraph.</p>' \
        '<img src="https://i.ytimg.com/vi/HQZxg6qlP9c/maxresdefault.jpg" width=200>'

@app.route("/bye")
@make_bold
@make_emph
@make_itallics
# @make_emphasis
# @make_underline
def bye():
    return "Bye!"

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello {name}! Happy {number} birthday"

if __name__ == "__main__":
    app.run(debug=True)