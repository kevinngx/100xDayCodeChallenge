from flask import Flask
import random

app = Flask(__name__)
random_number = random.randint(0,9)
print(random_number)

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
def main_page():
    return '<h1> Welcome to the numbers challenge! </h1> ' \
           '<p>Pick a number between 0 and 9</p>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'



# Different routes using @app.route

@app.route('/<int:guess>')
def guess_number(guess):
    if guess < random_number:
        return '<h1>Too low, try again!</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    elif guess > random_number:
        return '<h1>too high, try again!</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    else:
        return '<h1>SPOT ON!</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
    return 'Goodbye cruel world!!'

@app.route('/bye')
def bye_world():
    return 'Goodbye cruel world!!'


@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f'Hello {name + str(number)}'


if __name__ == "__main__":
    app.run(debug=True)
