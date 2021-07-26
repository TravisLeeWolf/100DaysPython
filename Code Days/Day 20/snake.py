from turtle import Turtle

# CONSTANTS
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_SPACES = 20
## Angle directions for the snake to move
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
        self.sections = []
        self.createSnake()
        self.head = self.sections[0]


    def createSnake(self):
        for position in STARTING_POSITIONS:
            self.addSectionToSnake(position)
            

    def addSectionToSnake(self, position):
        sectionOfSnake = Turtle("square")
        sectionOfSnake.color("white")
        sectionOfSnake.penup()
        sectionOfSnake.goto(position)

        self.sections.append(sectionOfSnake)

    def extend(self):
        self.addSectionToSnake(self.sections[-1].position())

    def move(self):
        for sectionNumber in range(len(self.sections) -1 , 0, -1):
            newXPosition = self.sections[sectionNumber - 1].xcor()
            newYPosition = self.sections[sectionNumber - 1].ycor()
            self.sections[sectionNumber].goto(newXPosition, newYPosition)
        self.sections[0].forward(MOVE_SPACES)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

