from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setheading(180)
        self.penup()
        self.pickRandomBodyColor()
        self.startAtRandomYPosition()
        self.carsSpeed = STARTING_MOVE_DISTANCE

    def pickRandomBodyColor(self):
        bodyColor = random.choice(COLORS)
        self.color(bodyColor)

    def startAtRandomYPosition(self):
        yPosition = random.randrange(-240, 240, 20)
        self.goto(300, yPosition)

    def speedUpCar(self):
        self.carsSpeed += MOVE_INCREMENT

    def moveForward(self):
        self.forward(self.carsSpeed)

    def hidePreviousCars(self):
        self.hideturtle()

