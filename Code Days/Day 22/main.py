# Made by @TravisLeeWolf

from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

# Setup the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
# Turn off screen update
screen.tracer(0)

# Setup paddles
rightPaddle = Paddle((350, 0))
leftPaddle = Paddle((-350, 0))
# Setup ball
ball = Ball()

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
    time.sleep(0.1)
    ball.move()

    # Detect when the ball hits the top or bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounceY()

    # Detect when the ball this the paddle
    if ball.distance(rightPaddle) < 50 and ball.xcor() > 320 or ball.distance(leftPaddle) < 50 and ball.xcor() < - 320:
        ball.bounceX()

# Exit game when screen is clicked, NOTE: Goes at the end
screen.exitonclick()