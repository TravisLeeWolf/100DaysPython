from flask import Flask, render_template, request, redirect, sessions, url_for
# import sqlite3
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# Creating database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

## Create table
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    #Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'
    
# db.create_all()

## Adding an entry
# new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9)
# db.session.add(new_book)
# db.session.commit()

all_books = db.session.query(Book).all()

# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating INTEGER NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template('index.html', booklist=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        bookName = request.form["bookName"]
        author = request.form["author"]
        rating = int(request.form["rating"])
        newBookEntry = Book(title=bookName, author=author, rating=rating)
        db.session.add(newBookEntry)
        db.session.commit()
        return redirect(url_for("home"))
    else:
        return render_template('add.html')

@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        bookID = request.form["id"]
        book_to_update = Book.query.get(bookID)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for("home"))
    bookID = request.args.get('id')
    bookSelected = Book.query.get(bookID)
    return render_template("edit.html", book=bookSelected)

@app.route("/delete")
def delete():
    bookID = request.args.get('id')
    bookToDelete = Book.query.get(bookID)
    db.session.delete(bookToDelete)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)

