from turtle import Screen, Turtle
from snake import Snake
import time

# 0. Game setup

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The UNSW BSOC Experience")
screen.tracer(0)

snake = Snake()

screen.listen()

# Arrow Key Options
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# WAS Option
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_is_on = True
while game_is_on:
    
    screen.update()
    time.sleep(0.1)
    snake.move()

# 3. Control the snake 

# 4. Make food mechanic

# 5. Create a scoreboard

# 6. Detect collision with wall 

# 7. Collision with its tail

screen.exitonclick()