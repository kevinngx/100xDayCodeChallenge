from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1,10)
    return render_template("index.html", num=random_number, year=datetime.date.today().year)

@app.route('/guess/<string:input_name>')
def guess(input_name):
    gender_guess = requests.get(f'https://api.genderize.io?name={input_name}').json()['gender']
    age_guess = requests.get(f'https://api.agify.io?name={input_name}').json()['age']
    nationality_guess = requests.get(f'https://api.nationalize.io?name={input_name}').json()['country'][0]['country_id']

    return render_template("guess.html", name=input_name, gender=gender_guess, age=age_guess, nationality=nationality_guess)

@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/5d2debf7b8858bebb875"
    response = requests.get(blog_url)
    all_posts = response.json()
    # print(all_posts)
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)


