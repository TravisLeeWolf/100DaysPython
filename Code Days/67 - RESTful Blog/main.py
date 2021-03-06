from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['CKEDITOR_PKG_TYPE'] = 'basic'
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    # Using CKEditor for the body
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


@app.route('/')
def get_all_posts():
    posts = db.session.query(BlogPost).all()
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:post_id>")
def show_post(post_id):
    requested_post = BlogPost.query.get(post_id)
    return render_template("post.html", post=requested_post)


@app.route("/new-post", methods=["GET", "POST"])
def createNewPost():
    if request.method == "POST":
        title = request.form["title"]
        subtitle = request.form["subtitle"]
        author = request.form["author"]
        img_url = request.form["img_url"]
        body = request.form["body"]
        time = datetime.now().strftime("%B%d, %Y")
        newPostEntry = BlogPost(title=title, subtitle=subtitle, author=author, img_url=img_url, body=body, date=time)
        db.session.add(newPostEntry)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    form = CreatePostForm()
    return render_template("make-post.html", form=form, postType="New Post")


@app.route("/edit-post/<post_id>", methods=["GET", "POST"])
def editPost(post_id):
    currentPost = BlogPost.query.get(post_id)
    if request.method == "POST":
        currentPost.title = request.form["title"]
        currentPost.subtitle = request.form["subtitle"]
        currentPost.author = request.form["author"]
        currentPost.img_url = request.form["img_url"]
        currentPost.body = request.form["body"]
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    form = CreatePostForm(
        title = currentPost.title,
        subtitle = currentPost.subtitle,
        author = currentPost.author,
        img_url = currentPost.img_url,
        body = currentPost.body
    )
    return render_template("make-post.html", form=form, postType="Edit Post")

@app.route("/delete")
def deletePost():
    post_id = request.args.get("post_id")
    postToDelete = BlogPost.query.get(post_id)
    db.session.delete(postToDelete)
    db.session.commit()
    return redirect(url_for("get_all_posts"))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)