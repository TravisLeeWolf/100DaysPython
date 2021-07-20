# Made by TravisLeeWolf

#import turtle
# Aliasing a module
import turtle as t

# Construct object
my_turtle = t.Turtle()

# Write method to create a 100x100 square
for _ in range(15):
    my_turtle.pendown()
    my_turtle.forward(20)
    my_turtle.penup()
    my_turtle.forward(20)


my_screen = t.Screen()
my_screen.exitonclick()
# Display screen goes at the end