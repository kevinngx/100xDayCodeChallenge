from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap

class login_form(FlaskForm):
    username = StringField(label='username', validators=[DataRequired(), Email("Must be a valid email")])
    password = StringField(label='password', validators=[DataRequired(), Length(5, 10, "Must be between 1 and 10 characters")])
    submit = SubmitField(label='LOG IN')
    WTF_CSRF_SECRET_KEY = 'a random string'


app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"
Bootstrap(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = login_form()

    if request.method == "POST":
        form = login_form()
        if form.validate_on_submit():
            print(form.username.data)
            print(form.password.data)
            if form.username.data == "admin@email.com" and form.password.data == "12345678":
                return render_template('success.html')
            else :
                return render_template('denied.html')        

    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True, port=4040)
    