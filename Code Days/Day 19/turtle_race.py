# Made by @TravisLeeWolf

from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make a bet", prompt="Which turtle will win the race? Enter a color: ")

# TODO: Make a list of rainbow colors
## Assign colors to individual turtles
## Send them to the start

screen.exitonclick()