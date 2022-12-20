from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie-ratings.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    title = db.Column(db.String(250),  unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500),  nullable=False)
    rating = db.Column(db.String(250), nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(500),  nullable=False)
    img_url = db.Column(db.String(250),  nullable=False)

class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    ranking = StringField("How does this film rank on your list?")
    submit = SubmitField("Done")

class NewMovieForm(FlaskForm):
    title = StringField("Film Title")
    year = StringField("Year of Release")
    description = StringField("Description")
    rating = StringField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    ranking = StringField("How does this film rank on your list?")
    img_url = StringField("Link to Poster")
    submit = SubmitField("Add")
    
with app.app_context():
    db.create_all()
    # new_movie = Movie(
    #     title="Phone Booth",
    #     year=2002,
    #     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    #     rating=7.3,
    #     ranking=10,
    #     review="My favourite character was the caller.",
    #     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
    # )

    # new_movie = Movie(
    #     title="Drive",
    #     year=2011,
    #     description="A mysterious Hollywood stuntman and mechanic moonlights as a getaway driver and finds himself in trouble when he helps out his neighbor in this action drama.",
    #     rating=7.5,
    #     ranking=1,
    #     review="Cute main character<3",
    #     img_url="https://i.ebayimg.com/images/g/mvMAAOSw5cNYLe15/s-l400.jpg"
    # )

    # db.session.add(new_movie)
    # db.session.commit()

@app.route("/", methods=["GET", "POST"])
def home():

    # Delete movie
    delete_id = request.args.get("delete_id")
    if delete_id != None:
        print(f'Deletion ID = {delete_id}')
        movie = Movie.query.get(delete_id)
        db.session.delete(movie)
        db.session.commit()

    with app.app_context():
        all_movies = db.session.query(Movie).all()
    print(all_movies)
    return render_template("index.html", all_movies=all_movies)

@app.route("/add", methods=["GET", "POST"])
def add():
    form = NewMovieForm()
    if form.validate_on_submit():
        print('*****************')
        movie = Movie()
        movie.title = form.title.data
        movie.year = int(form.year.data)
        movie.description = form.description.data
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        movie.ranking = int(form.ranking.data)
        movie.img_url = form.img_url.data
        db.session.add(movie)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html", form=form)

@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)
    if form.validate_on_submit():
        print('*****************')
        print(movie)
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        movie.ranking = int(form.ranking.data)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("edit.html", movie=movie, form=form)

@app.route("/select")
def select():
    return render_template("select.html")


if __name__ == '__main__':
    app.run(debug=True)
