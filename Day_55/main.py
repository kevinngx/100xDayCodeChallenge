from flask import Flask
import random

app = Flask(__name__)

def make_bold(function):
    def wrapper_func():
        return f'<b>{function()}</b>'

    return wrapper_func


def make_emphasis(function):
    def wrapper_func():
        return f'<em>{function()}</em>'

    return wrapper_func


def make_underline(function):
    def wrapper_func():
        return f'<u>{function()}</u>'

    return wrapper_func


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center"> Hello, World! </h1> ' \
           '<p>This is a paragraph tag</p>' \
           '<img src="https://i.pinimg.com/originals/91/e3/aa/91e3aa2fb1b9d9fa0e99ab1aceb8cc0b.jpg">'


# Different routes using @app.route

@app.route('/bye')
@make_bold
@make_emphasis
@make_underline
def bye_world():
    return 'Goodbye cruel world!!'


@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f'Hello {name + str(number)}'


if __name__ == "__main__":
    app.run(debug=True)
