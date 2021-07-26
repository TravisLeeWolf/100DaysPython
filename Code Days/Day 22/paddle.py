from turtle import Turtle

MOVE_SPACES = 20

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.speed("fastest")
        self.goto(position)

    def moveUp(self):
        newYPosition = self.ycor() + MOVE_SPACES
        self.goto(self.xcor, newYPosition)

    def moveDown(self):
        newYPosition = self.ycor() - MOVE_SPACES
        self.goto(self.xcor, newYPosition)


