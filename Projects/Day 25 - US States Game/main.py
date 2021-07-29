import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

# Adding the image to turtle
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# Get guess, make sure to convert to title case
answerState = screen.textinput(title="Guess the State", prompt="What's another state name?").title()

stateData = pandas.read_csv("50_states.csv")
# Check if guess is among the 50 states
guessState = stateData[stateData.state == answerState]
if guessState.empty:
    print("Try again")
else:
    # Write correct guess onto the map
    print(guessState)

# Use a loop to allow user to keep guessing
# Record the correct guesses in a list
# Keep track of the score

screen.exitonclick()