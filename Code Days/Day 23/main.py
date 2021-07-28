from hashlib import new
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

# Instance in the player and scoreboard
player = Player()
scoreboard = Scoreboard()
scoreboard.displayLevel()

# Listen for player input
screen.listen()
screen.onkeypress(player.moveForward, "Up")

# Game loop
gameIsOn = True
gameLoopCount = 0
gameLevel = 0

carsOnRoad = []

def checkIfTouchingPlayer(car):
    if car.distance(player) < 30:
        global gameIsOn
        gameIsOn = False
        scoreboard.gameIsOver()

def moveAllCars(carList):
    """Take a list of car objects and moves them foward using the object function object.moveForward()"""
    for car in carList:
        car.moveForward()
        checkIfTouchingPlayer(car)

while gameIsOn:
    time.sleep(0.1)
    screen.update()
    # Randomly instance in cars, NOTE: new car is spawned every 6th game loop
    if gameLoopCount == 6:
        newCar = CarManager()
        carsOnRoad.append(newCar)
        for _ in range(gameLevel):
            newCar.speedUpCar()
        moveAllCars(carsOnRoad)
        gameLoopCount = 0
    else:
        gameLoopCount += 1
        moveAllCars(carsOnRoad)
    # Check if player reached the goal then go to next level
    if player.pos()[1] > player.finishLineY:
        player.goBackToStart()
        for car in carsOnRoad:
            car.hidePreviousCars()
        carsOnRoad = []
        scoreboard.nextLevel()
        gameLevel += 1


screen.update()
screen.exitonclick()
