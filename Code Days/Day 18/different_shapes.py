# Made by TravisLeeWolf

#import turtle
# Aliasing a module
import turtle as t


# Construct object
my_turtle = t.Turtle()


# Write method to create a 100x100 square
colors = ["red","yellow","pink","green","purple","orange", "blue"]
# You can use
#for angle in range(3,11):
for angle in range(7):
    angle = angle + 3
    my_turtle.pencolor(colors[angle - 3])
    shape_angle = 360 / angle
    for _ in range(angle):
        my_turtle.forward(100)
        my_turtle.right(shape_angle)
    

my_screen = t.Screen()
my_screen.exitonclick()
# Display screen goes at the end