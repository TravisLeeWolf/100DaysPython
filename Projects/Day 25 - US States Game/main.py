import turtle
import pandas
from statesWriter import StatesWriter

screen = turtle.Screen()
screen.setup(width=729, height=495)
screen.bgcolor("black")
screen.title("U.S. States Game")


# Adding the image to turtle
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Load in csv data
data = pandas.read_csv("50_states.csv")

# Instance in writer
writer = StatesWriter()

# Use a loop to allow user to keep guessing
gameIsOn = True

# Record the correct guesses in a list
correctlyGuessedStates = []
inputTitleForMessages = "Guess the state"
inputPromptToDisplayScore = "Type in a state to guess."
score = 0

while gameIsOn:
    # Get user guess and conver to title case
    guess = screen.textinput(title=inputTitleForMessages, prompt=inputPromptToDisplayScore)
    guess = guess.title()

    # Check if guess is among the 50 states
    matchedToGuess = data[data.state == guess]
    if matchedToGuess.empty:
        inputTitleForMessages = "Try another guess"
    else:
        if guess in correctlyGuessedStates:
            inputTitleForMessages = "Already guessed"
        else:
            # Write correct guess onto the map
            name = matchedToGuess.state.item()
            x = matchedToGuess.x.item()
            y = matchedToGuess.y.item()
            writer.goToState(xPosition=x, yPosition=y)
            writer.writeStateName(stateName=name)
            inputTitleForMessages = "Keep going!"
            # Keep track of the score
            if score == 50:
                gameIsOn = False
                print("You've guessed all 50 states!")
            else:
                score += 1
                inputPromptToDisplayScore = f"You've guessed ({score}/50)"
                

screen.exitonclick()