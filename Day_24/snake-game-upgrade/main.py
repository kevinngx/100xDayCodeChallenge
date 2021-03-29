from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# 0. Game setup

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The UNSW BSOC Experience")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# 3. Control the snake 

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

    # 4. Make food mechanic

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.add_point()
        print("nom nom nom")

    # 7. Collision with its tail
    for segment in snake.segments[1:-1]:
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            scoreboard.reset()
            snake.reset()

screen.exitonclick()