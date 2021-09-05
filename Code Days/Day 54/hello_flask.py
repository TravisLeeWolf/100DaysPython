from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# NOTE: Setting up the environment using powershell
## py -m venv env
## env\Scripts\activate
## pip install flask
## $env:FLASK_APP = "program.py"
## flask run

## Ctrl + C (To close the server)