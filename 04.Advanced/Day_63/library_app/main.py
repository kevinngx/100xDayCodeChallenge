from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import sqlite3
from flask_sqlalchemy import SQLAlchemy

# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collections.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CREATE TABLE

class books(db.Model):
    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    title = db.Column(db.String(250),  nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<books %r>' % self.title

with app.app_context():
    db.create_all()
    # new_book = books(title="Harry Potter", author="J. K. Rowling", rating=10)
    # db.session.add(new_book)
    # db.session.commit()

class BookForm(FlaskForm):
    name = StringField('Book Name', validators=[DataRequired()])
    author = StringField('Book Author', validators=[DataRequired()])
    rating = StringField('Book Rating', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/')
def home():
    with app.app_context():
        all_books = db.session.query(books).all()
    print(all_books)
    return render_template('index.html', all_books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = BookForm()
    if request.method == "POST":
        if form.validate_on_submit():
            print("Success, adding book to database")
            with app.app_context():
                new_book = books(title=form.name.data, author=form.author.data, rating=form.rating.data)
                db.session.add(new_book)
                db.session.commit()
            return render_template('add.html', form=form, success=True)

    print("Rendering new form template")
    return render_template('add.html', form=form, success=False)


if __name__ == "__main__":
    app.run(debug=True)



