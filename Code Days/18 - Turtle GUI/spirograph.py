import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

screen = t.Screen()
screen.bgcolor("gray10")

def random_color():
    r = random.randint(155, 255)
    g = random.randint(155, 255)
    b = random.randint(155, 255)
    color = (r, g, b)
    return color

tim.speed("fastest")
tim.pensize(1.5)

########### Challenge 5 - Spirograph ########
# method without different degrees
# direction = 0
# for _ in range(37):
#     tim.pencolor(random_color())
#     tim.circle(100)
#     tim.setheading(direction)
#     direction += 10

def draw_spirograph(degrees):
    for _ in range(int(360 / degrees)):
        tim.pencolor(random_color())
        tim.circle(150)
        tim.setheading(tim.heading() + degrees)

draw_spirograph(5)

screen.exitonclick()
