from datetime import time
from flask import Flask
from flask import render_template
from random import randint
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    randNum = randint(1, 10)
    footerYear = datetime.now().year
    return render_template("index.html", randNum=randNum, year=footerYear)

if __name__ == "__main__":
    app.run(debug=True)