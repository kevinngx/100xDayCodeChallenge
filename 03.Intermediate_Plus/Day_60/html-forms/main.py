from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def get_home():    
    return render_template("index.html")

@app.route('/login', methods=["POST"])
def login():
    if request.method == 'POST':
        user = request.form['name']
        password = request.form['password']
        print(f'User = {user}\nPass={password}')
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=4444)