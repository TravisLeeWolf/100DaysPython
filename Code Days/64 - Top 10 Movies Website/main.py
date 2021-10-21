from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from movie_search import MovieSearch

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

# Creating our movie database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Create table
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String)
    img_url = db.Column(db.String)

    # Allows each movie object to be identified by its title when printed.
    def __repr__(self):
        return f'<Movie {self.title}>'
    
# db.create_all() # This creates a new database, only needs to be run once

## Adding a new movie manually
# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# db.session.add(new_movie)
# db.session.commit()

# Update Movie Form
class updateMovie(FlaskForm):
    rating = StringField(label="Your rating out of 10 e.g. 7.5", validators=[DataRequired()])
    review = StringField(label="Your review", validators=[DataRequired()])
    submit = SubmitField(label="Done")

# Add Movie Form
class addMovie(FlaskForm):
    name = StringField(label="Movie Title", validators=[DataRequired()])
    submit = SubmitField(label="Add Movie")

# Initiate MovieSearch
movieSearcher = MovieSearch()

@app.route("/")
def home():
    movies = db.session.query(Movie).all()
    return render_template("index.html", movieList=movies)

@app.route("/update", methods=["GET", "POST"])
def edit():
    movieID = request.args.get("id")
    movieSelected = Movie.query.get(movieID)
    form = updateMovie()
    if request.method == "POST":
        if form.validate_on_submit():
            movieSelected.rating = form.rating.data
            movieSelected.review = form.review.data
            db.session.commit()
            return redirect(url_for("home"))
    return render_template("edit.html", movie=movieSelected, form=form)

@app.route("/delete")
def delete():
    movieID = request.args.get('id')
    movieToDelete = Movie.query.get(movieID)
    db.session.delete(movieToDelete)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/add", methods=["GET", "POST"])
def add():
    form = addMovie()
    if request.method == "POST":
        if form.validate_on_submit():
            movieData = movieSearcher.searchMovie(movieTitle=form.name.data)
            return render_template("select.html", movieData=movieData)
    return render_template("add.html", form=form)

@app.route("/details")
def addToDatabase():
    movieID = request.args.get('id')
    print(movieID)
    movieSearcher.getMovieDetails(movieID)
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)
