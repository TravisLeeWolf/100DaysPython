# Made by TravisLeeWolf

#import turtle
# Aliasing a module
import turtle as t

# Construct object
my_turtle = t.Turtle()

# Write method to create a 100x100 square
for _ in range(4):
    my_turtle.forward(100)
    my_turtle.right(90)

my_screen = t.Screen()
my_screen.exitonclick()
# Display screen goes at the end
