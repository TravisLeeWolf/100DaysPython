# Made by @TravisLeeWolf

from turtle import Turtle, Screen
from random import randint

# For when the race starts
is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make a bet", prompt="Which turtle will win the race? Enter a color: ")

# Make a list of rainbow colors
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
y_pos = [-120, -80, -40, 0, 40, 80, 120]
# List of racers
all_racers = []

for turtle_index in range(0, 7):
    racer = Turtle(shape="turtle")
    # Assign colors to individual turtles
    racer.color(colors[turtle_index])
    racer.penup()
    # Send them to the start
    racer.goto(x=-230, y=y_pos[turtle_index])
    all_racers.append(racer)

if user_bet:
    is_race_on = True

while is_race_on:
    for racer in all_racers:
        if racer.xcor() > 230:
            is_race_on = False
            winning_color = racer.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost. The {winning_color} turtle is the winner.")
        rand_distance = randint(0, 10)
        racer.forward(rand_distance)


screen.exitonclick()