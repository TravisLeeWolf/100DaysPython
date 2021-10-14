from flask import Flask, render_template
import requests
from post import Post

POSTS_URL = "https://api.npoint.io/ed99320662742443cc5b"
posts = requests.get(POSTS_URL).json()
postObjects = []
for post in posts:
    postObject = Post(post["id"], post["title"], post["subtitle"], post["body"])
    postObjects.append(postObject)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts=postObjects)

@app.route("/post/<int:index>")
def showPost(index):
    requestedPost = None
    for blogPost in postObjects:
        if blogPost.id == index:
            requestedPost = blogPost
    return render_template("post.html", post=requestedPost)

if __name__ == "__main__":
    app.run(debug=True)