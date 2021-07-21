import turtle as t
import random

tim = t.Turtle()

########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
heading_in = [0, 90, 180, 360]

# Change thickness of line
tim.pensize(10)
tim.speed("fast")
# Randomize color after each stroke
# Turn a random direction (up, down, left, right) and draw a line
# Keep going 50 times
for _ in range(100):
    tim.pencolor(random.choice(colours))
    tim.setheading(random.choice(heading_in))
    tim.forward(20)

# Show screen at the end
screen = t.Screen()
screen.exitonclick()