MOVE_DISTANCE = 20
BOARD_HEIGHT = 600
BOARD_LENGTH = 1000
UP = 90
DOWN = 270
from turtle import Turtle

class Paddle(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    
    def down(self):
        pass
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    