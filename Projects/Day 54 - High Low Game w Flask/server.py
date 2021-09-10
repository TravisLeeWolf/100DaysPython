from flask import Flask
from random import randint

GREETING = """
    <!DOCTYPE html>
    <head>
        <title>Higher lower game</title>
    </head>
    <body>
        <div style='text-align: center;'>
            <h1>Guess a number between 1 and 10</h1>
            <img src='https://media4.giphy.com/media/a5viI92PAF89q/giphy.gif?cid=ecf05e47ehnhaubknja53al1jjjkbmtl1axsp2t5ukgrifu2&rid=giphy.gif&ct=g' alt='Batman Thinking' width='400'>
        </div>
    </body>
    """

TRY_AGAIN = """
    <!DOCTYPE html>
    <head>
        <title>Try again</title>
    </head>
    <body>
        <div style='text-align: center;'>
            <h1 style='color: red;'>That's not it, try again</h1>
            <img src='https://media2.giphy.com/media/Qumf2QovTD4QxHPjy5/200.webp?cid=ecf05e47qrqx50hcyxz1k832ttu5e5uic66i9avss5fpfmwl&rid=200.webp&ct=g' alt='Batman Slap' width='400'>
        </div>
    </body>
    """

CORRECT_ANSWER = """
    <!DOCTYPE html>
    <head>
        <title>Correct!</title>
    </head>
    <body>
        <div style='text-align: center;'>
            <h1 style='color: green;'>You guessed the right answer!</h1>
            <img src='https://media0.giphy.com/media/pSFEEQMaNcFAQ/200.webp?cid=ecf05e476h2ols3387pzmtxd7pz6cyopvy98x83cpizm1zrr&rid=200.webp&ct=g' alt='Batman Slap' width='400'>
        </div>
    </body>
    """

app = Flask(__name__)

@app.route("/")
def gameGreeting():
    return GREETING

def pickRandomNumber():
    numberToGuess = randint(1,10)
    return numberToGuess

answer = pickRandomNumber()
print(answer)

@app.route("/<guess>")
def checkGuess(guess):
    try:
        guess = int(guess)
    except:
        print("Type a single number from 1 to 10")
    finally:
        if guess == answer:
            return CORRECT_ANSWER
        else:
            return TRY_AGAIN
if __name__ == "__main__":
    app.run(debug=True)