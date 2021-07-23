# Made by @TravisLeeWolf

from turtle import Screen, Turtle
import time

# Setup the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
# Turning off the screen update
screen.tracer(0)

starting_pos = [(0, 0), (-20, 0), (-40, 0)]

sections = []

# Create 3 turtles one after the other
for position in starting_pos:
    snake_section = Turtle("square")
    snake_section.color("white")
    snake_section.penup()
    snake_section.goto(position)

    sections.append(snake_section)

game_is_on = True
while game_is_on:
    # The reason we add screen update here is so that it updates after all sections have moved
    screen.update()
    time.sleep(0.1) # Decreasing the sleep time changes how quickly the snake moves
    # Statements to allow sections to follow the 'head'
    for sect_num in range(len(sections) -1 , 0, -1):
        new_x = sections[sect_num - 1].xcor()
        new_y = sections[sect_num - 1].ycor()
        sections[sect_num].goto(new_x, new_y)
    sections[0].forward(20)
    

screen.exitonclick()
# This goes at the end