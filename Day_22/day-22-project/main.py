import random
from turtle import Turtle, Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time

def setup_board():
    line_turtle = Turtle()
    line_turtle.color("white")
    line_turtle.penup()
    line_turtle.goto(-1,230)
    line_turtle.pendown()
    line_turtle.right(90)
    line_turtle.width(3)
    for i in range(0, 13):
        line_turtle.forward(20)
        line_turtle.penup()
        line_turtle.forward(20)
        line_turtle.pendown()

# 0. Game setup
screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("PeepeepooPONG")
screen.tracer(0)
setup_board()
screen.listen()
    
# 2. Create and move a paddle
player_1 = Paddle((-450,0))
screen.onkey(player_1.up, "w")
screen.onkey(player_1.down, "s")

# 3. Create another paddle
player_2 = Paddle((450, 0))
screen.onkey(player_2.up, "Up")
screen.onkey(player_2.down, "Down")

# 8. Keep score
scoreboard = Scoreboard()


# 4. Create the ball and make it move
ball = Ball()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

# 5. Detect collision with wall and bounce
# 6. Detect collision with paddle
# 7. Dtect when paddle misses



screen.exitonclick()

