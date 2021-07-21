import turtle as t
import random

tim = t.Turtle()
screen = t.Screen()
screen.bgcolor("gray10")

########### Challenge 4 - Random Walk ########
#colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# Let's add some randomization to the color choice
t.colormode(255)
def random_color():
    r = random.randint(100, 255)
    g = random.randint(100, 255)
    b = random.randint(100, 255)
    color = (r,g,b)
    return color

heading_in = [0, 90, 180, 270]

# Change thickness of line
tim.pensize(10)
tim.speed("fastest")
# Randomize color after each stroke
# Turn a random direction (up, down, left, right) and draw a line
# Keep going 50 times
for _ in range(100):
    tim.pencolor(random_color())
    tim.setheading(random.choice(heading_in))
    tim.forward(20)

# Show screen at the end
screen.exitonclick()