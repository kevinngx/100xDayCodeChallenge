from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect, create_engine
from sqlalchemy.pool import StaticPool
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    # called using Cafe.to_dict() to return dictionary version of object
    def to_dict(self):
        dictionary = {}
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
        return dictionary

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random")
def get_random_cafe():
    # Get a random cafe
    cafe_data = db.session.query(Cafe).all()
    cafe = random.choice(cafe_data)

    # Convert Cafe object into a json response string
    response = jsonify(cafe=cafe.to_dict())
    return response

@app.route("/all")
def get_all_cafe():
    # Get a random cafe
    cafe_data = db.session.query(Cafe).all()

    # Convert cafe_data (list of Cafe objects) into a json response string
    response = jsonify(cafes=[cafe.to_dict() for cafe in cafe_data])
    return response

@app.route("/search")
def search_cafe():
    # cafe_location = request.args.get('location')
    query_location = request.args.get("loc")
    cafe_data = db.session.query(Cafe).filter_by(location=query_location).all()
    
    response = jsonify(cafes=[cafe.to_dict() for cafe in cafe_data])
    return response

@app.route("/add", methods = ['POST'])
def add_new_cafe():
    new_cafe = Cafe(
        name=request.args.get("name"),
        map_url=request.args.get("map_url"),
        img_url=request.args.get("img_url"),
        location=request.args.get("location"),
        has_sockets=bool(request.args.get("has_sockets")),
        has_toilet=bool(request.args.get("has_toilet")),
        has_wifi=bool(request.args.get("has_wifi")),
        can_take_calls=bool(request.args.get("can_take_calls")),
        seats=request.args.get("seats"),
        coffee_price=request.args.get("coffee_price")
    )
    db.session.add(new_cafe)
    db.session.commit()

    response = jsonify(response={"success": "Successfully added the new cafe"})
    return response

@app.route("/update_price/<cafe_id>", methods = ['PATCH'])
def update_coffe_price(cafe_id):
    new_price = request.args.get("new_price")
    print(f'Updating Cafe ID:{cafe_id} with new price {new_price}')
    
    # Update price in database
    cafe = Cafe.query.get(cafe_id)
    if cafe == None :
        response = jsonify(error={"Not Found": "Sorry a cafe with that ID was not found"}), 404
    else:
        cafe.coffee_price = new_price
        db.session.commit()
        response = jsonify(response={"success": "Successfully updated the cafe price"}), 200

    return response

@app.route("/delete/<cafe_id>", methods = ['DELETE'])
def delete_cafe(cafe_id):

    if request.args.get("api-key") != "TopSecretAPIKey":
        response = jsonify(error={"Unauthorised Access": "Sorry you are not authorised to delete cafes"}), 403
    else:
        print(f'Deleting Cafe ID:{cafe_id}')
        cafe = Cafe.query.get(cafe_id)
        if cafe == None :
            response = jsonify(error={"Not Found": "Sorry a cafe with that ID was not found"}), 404
        else:
            # TODO: Delete record
            print("DELETING")
            db.session.delete(cafe)
            db.session.commit()
            response = jsonify(response={"success": "Successfully deleted cafe"}), 200

    return response
    

## HTTP GET - Read Record

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
