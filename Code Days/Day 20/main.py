# Made by @TravisLeeWolf

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

# Setup the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
# Turning off the screen update
screen.tracer(0)


snake = Snake()
food = Food()
scoreBoard = ScoreBoard()

# Take keyboard inputs and get the snake to turn
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

gameIsOn = True
while gameIsOn:
    # The reason we add screen update here is so that it updates after all sections have moved
    screen.update()
    time.sleep(0.1) # Decreasing the sleep time changes how quickly the snake moves
    
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreBoard.addToScore() 

screen.exitonclick()
# This goes at the end