import turtle
import pandas
from statesWriter import StatesWriter

screen = turtle.Screen()
screen.title("U.S. States Game")

# Adding the image to turtle
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Load in csv data
data = pandas.read_csv("50_states.csv")

# Instance in writer
writer = StatesWriter()

# Get user guess and conver to title case
guess = screen.textinput(title="Guess the State", prompt="What's another state name?")
guess = guess.title()

# Check if guess is among the 50 states
matchedToGuess = data[data.state == guess]
if matchedToGuess.empty:
    print("Try again")
else:
    # Write correct guess onto the map
    name = matchedToGuess.state.item()
    x = matchedToGuess.x.item()
    y = matchedToGuess.y.item()
    writer.goToState(xPosition=x, yPosition=y)
    writer.writeStateName(stateName=name)

# Use a loop to allow user to keep guessing
# Record the correct guesses in a list
# Keep track of the score

screen.exitonclick()