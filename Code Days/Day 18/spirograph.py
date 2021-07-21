import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint(100, 255)
    g = random.randint(100, 255)
    b = random.randint(100, 255)
    color = (r, g, b)
    return color

tim.speed(0)
tim.pensize(1.2)

########### Challenge 5 - Spirograph ########
direction = 0
for _ in range(37):
    tim.pencolor(random_color())
    tim.circle(100)
    tim.setheading(direction)
    direction += 10

screen = t.Screen()
screen.exitonclick()
