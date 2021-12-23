import turtle
import random

# Font statics
ALIGNMENT = "center"
FONT = ("BroshK-Plum", 200, "normal")

# Setup
text = turtle.Turtle()
screen = turtle.Screen()
text.hideturtle()

# Lists
numbers = ["1", "2", "3", "4", "5"]
letters = ["A", "B", "C", "D", "E"]
chosen = []

# Chooser
def chooser():
    choice = random.choice(letters) + random.choice(numbers)
    try:
        if choice in chosen:
            choice = chooser()
        else:
            chosen.append(choice)
        return choice
    except RecursionError:
        screen.bye()

def writeChoice(choice):
    text.clear()
    text.penup()
    text.write(f"{choice}", align=ALIGNMENT, font=FONT)

def pickOne():
    choice = chooser()
    writeChoice(choice)

turtle.onkey(pickOne, "space")
turtle.listen()

screen.exitonclick()