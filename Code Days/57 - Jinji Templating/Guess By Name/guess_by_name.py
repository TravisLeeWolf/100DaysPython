from flask import Flask
from flask import render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

def getGender(name):
    response = requests.get(f"https://api.genderize.io?name={name}")
    response.raise_for_status()
    data = response.json()
    gender = data["gender"]
    return gender

def getAge(name):
    response = requests.get(f"https://api.agify.io?name={name}")
    response.raise_for_status()
    data = response.json()
    age = data["age"]
    return age

@app.route("/<name>")
def makeGuess(name):
    gender = getGender(name)
    age = getAge(name)
    name = name.capitalize()
    return render_template("guess.html", name=name, gender=gender, age=age)

if __name__ == "__main__":
    app.run(debug=True)
