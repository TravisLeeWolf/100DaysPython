# Made by @TravisLeeWolf

from turtle import Turtle, Screen

tom = Turtle()
screen = Screen()

def move_forward():
    tom.forward(10)

def move_backward():
    tom.backward(10)

def turn_right():
    tom.right(10)

def turn_left():
    tom.left(10)

def clear_screen():
    screen.reset()
    tom.showturtle()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_right, "d")
screen.onkey(turn_left, "a")
screen.onkey(clear_screen, "c")
screen.exitonclick()