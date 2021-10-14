# Made by @TravisLeeWolf

# Import turtle
from turtle import Turtle, Screen

# Construct our turtle and screen
tim = Turtle()
screen = Screen()

# Function to move our turtle forward 50 spaces
def move_forward():
    tim.forward(50)

# Start the screen listener
screen.listen()
screen.onkey(move_forward, "space")
screen.exitonclick()
