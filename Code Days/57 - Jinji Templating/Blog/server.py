from flask import Flask
from flask import render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    blog_url = "https://api.npoint.io/ed99320662742443cc5b"
    response = requests.get(blog_url)
    response.raise_for_status()
    allPosts = response.json()
    return render_template("index.html", posts=allPosts)

@app.route("/about")
def aboutBlog():
    return render_template("about.html")

if __name__ == "__main__":
    app.run()