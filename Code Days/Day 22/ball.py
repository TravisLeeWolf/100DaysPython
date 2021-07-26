from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xMovement = 10
        self.yMovement = 10
        self.moveSpeed = 0.1

    def move(self):
        newXPosition = self.xcor() + self.xMovement
        newYPosition = self.ycor() + self.yMovement
        self.goto(newXPosition, newYPosition)

    def bounceY(self):
        self.yMovement *= -1

    def bounceX(self):
        self.xMovement *= -1
        self.moveSpeed *= 0.9

    def resetPosition(self):
        self.goto(0, 0)
        self.moveSpeed = 0.1
        self.bounceX()
    