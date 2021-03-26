from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.speed("fastest")
        self.penup()
        self.xtraject = 1
        self.ytraject = 1
    
    def move(self):
        new_x = self.xcor() + 10 * self.xtraject
        # 5. Detect collision with wall and bounce

        if self.ycor() + 10 > 300 or self.ycor() - 10 < -300:
            self.flip_y()
        new_y = self.ycor() + 10 * self.ytraject

        self.goto(new_x, new_y)

    def flip_x(self):
        self.xtraject *= -1
    
    def flip_y(self):
        self.ytraject *= -1
    
    def reset(self):
        self.goto((0,0))
        