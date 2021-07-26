from turtle import Turtle, penup, shape
from random import randint


class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fast")
        self.refresh()

    def refresh(self):
        randomXPosition = randint(-270, 270)
        randomYPosition = randint(-270, 270)
        self.goto(randomXPosition, randomYPosition)