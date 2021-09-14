from os import name
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def mainPage():
    person = "David"
    return render_template("index.html", name=person)

@app.route("/login", methods=["POST"])
def recieveData():
    userName = request.form["username"]
    userPass = request.form["password"]
    return f"<h2>Username: {userName}, Password: {userPass}</h2>"

if __name__ == "__main__":
    app.run(debug=True)