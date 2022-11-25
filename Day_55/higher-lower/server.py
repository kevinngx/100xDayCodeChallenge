from flask import Flask
import random

app = Flask(__name__)

# Generate a random number when the server is initiated
correct_number = random.randint(0,9)
print(f'Correct number is {correct_number}')

@app.route('/')
def home_page():
    return '<h1>Guess a number between 0 and 9</h1>' \
        '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

@app.route('/guess/<int:guess>')
def guess_page(guess):

    # Provide different results depending on the input
    if guess > correct_number: return f'<h1>Your guess was too high, try again!</h1> <img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">' 
    elif guess < correct_number: return f'<h1>Your guess was too low, try again!</h1> <img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">' 
    else: return f'<h1>You guessed {guess}</h1> <img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">' 

if __name__ == "__main__":
    app.run(debug=True)