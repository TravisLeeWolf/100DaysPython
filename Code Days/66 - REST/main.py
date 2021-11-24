from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
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

    def toDictionary(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record
@app.route("/random", methods=["GET"])
def getRandomCafe():
    allCafes = db.session.query(Cafe).all()
    randomCafe = random.choice(allCafes)
    return jsonify(cafe = randomCafe.toDictionary())


@app.route("/all", methods=["GET"])
def getAllCafes():
    allCafes = db.session.query(Cafe).all()
    return jsonify(cafes = [cafe.toDictionary() for cafe in allCafes])


@app.route("/search", methods=["GET"])
def getCafeAtLocation():
    queryLocation = request.args.get("loc")
    searchedCafe = db.session.query(Cafe).filter_by(location=queryLocation).first()
    if searchedCafe:
        return jsonify(cafe=searchedCafe.toDictionary())
    else:
        return jsonify(error={"Not found": "Sorry, we dont have a cafe at that location."})

## HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def postNewCafe():
    newCafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(newCafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


## HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def patchNewPrice(cafe_id):
    newPrice = request.args.get("new_price")
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe:
        cafe.coffee_price = newPrice
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}), 200
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404

## HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def deleteCafe(cafe_id):
    apiKey = request.args.get("api-key")
    if apiKey == "TopSecretAPIKey":
        cafe = db.session.query(Cafe).get(cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403


if __name__ == '__main__':
    app.run(debug=True)
