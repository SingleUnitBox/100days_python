from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

db = SQLAlchemy()
app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


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

    def to_dict(self):
        #Method 1.
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            #Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary

@app.route("/")
def home():
    pass
    

## HTTP GET - Read Record
@app.route("/random", methods=["GET"])
def get_random():
    with app.app_context():
        random_cafes = db.session.query(Cafe).all()
        random_cafe = random.choice(random_cafes)
        print(random_cafe)
    return jsonify(cafe=random_cafe.to_dict())
    #         (cafe={
    #     "id": random_cafe.id,
    #     "name": random_cafe.name,
    #     "map_url": random_cafe.map_url,
    #     "img_url": random_cafe.img_url,
    #     "location": random_cafe.location,
    #     "seats": random_cafe.seats,
    #     "has_toilet": random_cafe.has_toilet,
    #     "has_wifi": random_cafe.has_wifi,
    #     "has_sockets": random_cafe.has_sockets,
    #     "can_take_calls": random_cafe.can_take_calls,
    #     "coffee_price": random_cafe.coffee_price,
    # })

@app.route("/all", methods=["GET"])
def get_all():
    with app.app_context():
        cafes = []
        all_cafes = db.session.query(Cafe).all()
        for cafe in all_cafes:
            cafes.append(cafe.to_dict())
    return jsonify(cafes=cafes)

@app.route("/search", methods=["GET"])
def search():
    loc = request.args.get("loc")
    with app.app_context():
        cafe = db.session.query(Cafe).filter_by(location=loc).first()
        if cafe:
            return jsonify(cafe=cafe.to_dict())
        else:
            return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})

## HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
    name = request.form.get("name"),
    map_url = request.form.get("map_url"),
    img_url = request.form.get("img_url"),
    location = request.form.get("loc"),
    has_sockets = bool(request.form.get("sockets")),
    has_toilet= bool(request.form.get("toilet")),
    has_wifi= bool(request.form.get("wifi")),
    can_take_calls= bool(request.form.get("calls")),
    seats = request.form.get("seats"),
    coffee_price = request.form.get("coffee_price")
    )
    with app.app_context():
        db.session.add(new_cafe)
        db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})

## HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:id>", methods=["PATCH"])
def update_price(id):
    new_price = request.args.get("new_price")
    with app.app_context():
        cafe = db.session.query(Cafe).filter_by(id=id).first()
        if cafe:
            cafe.coffee_price = new_price
            db.session.commit()
            return jsonify(response={"success": "Successfully updated the price."})
        else:
            return jsonify(response={"Not Found": "Sorry a cafe with that id was not found in the database"})




## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
