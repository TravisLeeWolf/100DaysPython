from turtle import Turtle, clearscreen

ALIGNMENT = "center"
FONT = ("Pokemon GB", 12, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.displayScore()
        

    def displayScore(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def addToScore(self):
        self.score += 1
        self.clear()
        self.displayScore()