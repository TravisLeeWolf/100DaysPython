# Made by @TravisLeeWolf

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
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
# Setup score board
scoreboard = ScoreBoard()

# Take keyboard inputs
screen.listen()
# Right paddle movement
screen.onkeypress(rightPaddle.moveUp, "Up")
screen.onkeypress(rightPaddle.moveDown, "Down")
# Left paddle movement
screen.onkeypress(leftPaddle.moveUp, "w")
screen.onkeypress(leftPaddle.moveDown, "s")

gameIsOn = True
while gameIsOn:
    screen.update()
    time.sleep(ball.moveSpeed)
    ball.move()

    # Detect when the ball hits the top or bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounceY()

    # Detect when the ball this the paddle
    if ball.distance(rightPaddle) < 50 and ball.xcor() > 320 or ball.distance(leftPaddle) < 50 and ball.xcor() < - 320:
        ball.bounceX()

    # Detect when right paddle misses
    if ball.xcor() > 380:
        ball.resetPosition()
        scoreboard.leftGetsPoint()

    # Detect when left paddle misses
    if ball.xcor() < -380:
        ball.resetPosition()
        scoreboard.rightGetsPoint()


# Exit game when screen is clicked, NOTE: Goes at the end
screen.exitonclick()