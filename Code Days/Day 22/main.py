# Made by @TravisLeeWolf

from turtle import Screen
from paddle import Paddle

# Setup the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
# Turn off screen update
screen.tracer(0)

rightPaddle = Paddle((350, 0))
leftPaddle = Paddle((-350, 0))

# Take keyboard inputs
screen.listen()
# Right paddle movement
screen.onkey(rightPaddle.moveUp, "Up")
screen.onkey(rightPaddle.moveDown, "Down")
# Left paddle movement
screen.onkey(leftPaddle.moveUp, "w")
screen.onkey(leftPaddle.moveDown, "s")

gameIsOn = True
while gameIsOn:
    screen.update()

# Exit game when screen is clicked, NOTE: Goes at the end
screen.exitonclick()