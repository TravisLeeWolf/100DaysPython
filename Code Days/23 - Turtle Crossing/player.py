from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("Sea Green")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)
        self.finishLineY = FINISH_LINE_Y

    def moveForward(self):
        self.forward(MOVE_DISTANCE)

    def goBackToStart(self):
        self.goto(STARTING_POSITION)

