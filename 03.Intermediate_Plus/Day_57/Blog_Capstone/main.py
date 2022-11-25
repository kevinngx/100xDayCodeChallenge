from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    # Obtain the blog data in json format and pass it to the page
    blog_url = "https://api.npoint.io/5d2debf7b8858bebb875"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)

@app.route("/post/<int:blog_id>")
def get_post(blog_id):
    blog_url = "https://api.npoint.io/5d2debf7b8858bebb875"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("post.html", posts=all_posts, id=blog_id)

if __name__ == "__main__":
    app.run(debug=True)
