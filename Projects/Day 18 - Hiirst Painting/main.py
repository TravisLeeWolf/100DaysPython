# Made by TravisLeeWolf

# Imports
import turtle as t  # Turtle Graphics
import colorgram # Gets a color pallete from an image
import random # Random module

# Get color pallete
#colors = colorgram.extract('image.jpg', 12)
# NOTE: Fix FileNotFoundError: [Errno 2] No such file or directory: 'image.jpg' error

color_list = []
# Generate random colors until colorgram issue fixed
def random_color():
    r = random.randint(100, 255)
    g = random.randint(100, 255)
    b = random.randint(100, 255)
    color = (r, g, b)
    return color

for _ in range(32):
    color_list.append(random_color())

"""
Create a spot color drawing using Turtle
It's a 10 x 10 grid of colors
Each color is 20 in size and spaced 50 apart
"""
tim = t.Turtle()
t.colormode(255)

tim.pensize(20)
tim.speed(0)

screen = t.Screen()
screen.setup(750, 750)
screen.bgcolor("gray10")

y_position = -250
tim.penup()
tim.setposition(-250, y_position)

for _ in range(11):
    for _ in range(11):
        tim.pencolor(random.choice(color_list))
        tim.dot()
        tim.penup()
        tim.forward(50)
    y_position += 50
    tim.setposition(-250, y_position)
tim.hideturtle()
    

# Display the drawing
screen.exitonclick()