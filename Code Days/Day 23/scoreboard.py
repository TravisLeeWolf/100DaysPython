from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.goto(-290, 260)
        self.hideturtle()

    def displayLevel(self):
        self.write(f"Level: {self.level}", font=FONT)

    def gameIsOver(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

    def nextLevel(self):
        self.level += 1
        self.clear()
        self.displayLevel()

