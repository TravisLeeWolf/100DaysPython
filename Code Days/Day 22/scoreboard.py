from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.leftScore = 0
        self.rightScore = 0
        self.updateScoreBoard()

    def updateScoreBoard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.leftScore, align="center", font=("Pokemon GB", 36, "normal"))
        self.goto(100, 200)
        self.write(self.rightScore, align="center", font=("Pokemon GB", 36, "normal"))

    def leftGetsPoint(self):
        self.leftScore += 1
        self.updateScoreBoard()

    def rightGetsPoint(self):
        self.rightScore += 1
        self.updateScoreBoard()