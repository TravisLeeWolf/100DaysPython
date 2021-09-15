from flask import Flask, render_template, request
import requests
from post import Post
import smtplib

EMAIL_ADDRESS = ""
EMAIL_PASSWORD = ""

POSTS_URL = "https://api.npoint.io/88c2c1f644ef334058be"
posts = requests.get(POSTS_URL).json()
postObjects = []
for post in posts:
    postObject = Post(post["id"], post["title"], post["subtitle"], post["body"], post["date"])
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

@app.route('/about')
def showAbout():
    return render_template("about.html")

def sendMail(name, email, phone, message):
    message = f"{name} sent you an message.\n{message}\nYou can contact them at {email} or {phone}."
    try:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL_ADDRESS, password=EMAIL_PASSWORD)
            connection.sendmail(from_addr=EMAIL_ADDRESS,
                                to_addrs=EMAIL_ADDRESS,
                                msg=f"Subject:Message from {name}\n\n{message}")
    except:
        return "Issue with sending message."
    else:
        return "Message sent successfully!"

@app.route("/contact", methods=["GET", "POST"])
def contactPage():
    if request.method == "POST":
        data = request.form
        name = data["name"]
        email = data["email"]
        phone = data["phone"]
        message = data["message"]
        pageMessage = sendMail(name=name, email=email, phone=phone, message=message)
        return render_template("contact.html", contactMessage=pageMessage)
    else:
        pageMessage = "Contact Me"
        return render_template("contact.html", contactMessage=pageMessage)

if __name__ == "__main__":
    app.run(debug=True)

