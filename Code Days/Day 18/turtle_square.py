# Made by TravisLeeWolf

import turtle

# Construct object
my_turtle = turtle.Turtle()

# Write method to create a 100x100 square
for _ in range(4):
    my_turtle.forward(100)
    my_turtle.right(90)

my_screen = turtle.Screen()
my_screen.exitonclick()
# Display screen goes at the end
