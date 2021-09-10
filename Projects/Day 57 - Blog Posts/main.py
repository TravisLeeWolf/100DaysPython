from flask import Flask, render_template
import requests

POSTS_URL = "https://api.npoint.io/ed99320662742443cc5b"

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get(POSTS_URL)
    response.raise_for_status()
    postData = response.json()
    return render_template("index.html", posts=postData)

if __name__ == "__main__":
    app.run(debug=True)