from turtle import Turtle

FONT = ("Courier", 8, "normal")

class StatesWriter(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def goToState(self, xPosition, yPosition):
        self.goto(x=xPosition, y=yPosition)

    def writeStateName(self, stateName):
        dotAndName = "👇" + stateName
        self.write(dotAndName, font=FONT)