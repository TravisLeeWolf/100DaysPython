from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, in the URL type /result to see the code result.</p>"

def makeBold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def makeItalic(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def makeUnderlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

@app.route("/result")
@makeBold
@makeItalic
@makeUnderlined
def greetUser():
    return f"<p>This text has been styled using decorators.</p>"

if __name__ == "__main__":
    app.run()