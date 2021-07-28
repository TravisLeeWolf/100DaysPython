from turtle import Turtle, clearscreen

ALIGNMENT = "center"
FONT = ("Pokemon GB", 14, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as dataFile:
            self.highScore = int(dataFile.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.updateScoreboard()
        
    
    def updateScoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highScore}", align=ALIGNMENT, font=FONT)    

    def resetScore(self):
        if self.score > self.highScore:
            self.highScore = self.score
            with open("data.txt", mode="w") as dataFile:
                dataFile.write(str(self.highScore))
        self.score = 0
        self.updateScoreboard()
    
    def addToScore(self):
        self.score += 1
        self.updateScoreboard()

    
