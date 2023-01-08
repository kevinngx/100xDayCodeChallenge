from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/files/'
db = SQLAlchemy(app)

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB. 
# db.create_all()


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=["GET", "POST"])
def register():
    
    if request.method == "POST":
        print("POST")
        new_user = User(
            email = request.form.get("email"),
            password = generate_password_hash(request.form.get("password"), method='pbkdf2:sha256', salt_length=8),
            name = request.form.get("name")
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("secrets"))
    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        user = User.query.filter_by(email=request.form.get("email")).first()
        print(f'User = {user}')
        if user == None:
            error = 'No User Found'
        else:
            if check_password_hash(user.password, request.form.get("password")):
                login_user(user)
                return redirect(url_for('secrets'))
            else:
                error = 'Invalid credentials'
    return render_template("login.html", logged_in=current_user.is_authenticated, error=error)


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", logged_in=current_user.is_authenticated)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download/<filename>')
@login_required
def download(filename):
    print(f'Downloading file {filename}...')
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
