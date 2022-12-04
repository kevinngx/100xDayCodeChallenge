from flask import Flask, render_template, request
import requests

app = Flask(__name__)

posts = requests.get("https://api.npoint.io/cc413ba8b8622859ddbb").json()

@app.route('/')
def get_home():    
    return render_template("index.html", posts=posts)

@app.route('/about')
def get_about():
    return render_template("about.html")

@app.route('/contact', methods=['POST', 'GET'])
def get_contact():
    if request.method == 'POST':
        print("Success!")
        # return render_template("contact_success.html")    
        return render_template("contact.html", submitted=True)
    return render_template("contact.html", submitted=False)

@app.route('/post/<int:blog_id>')
def get_post(blog_id):
    for blog_post in posts:
        if blog_post["id"] == blog_id:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=4444)