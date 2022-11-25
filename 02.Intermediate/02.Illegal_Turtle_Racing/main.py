from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

# Get user input
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ").lower()
print(user_bet)

# Set up the board
red_turtle = Turtle()
red_turtle.color("red")
red_turtle.shape("turtle")
red_turtle.penup()
red_turtle.goto(-200, 150)

blue_turtle = Turtle()
blue_turtle.color("blue")
blue_turtle.penup()
blue_turtle.shape("turtle")
blue_turtle.goto(-200, 50)

green_turtle = Turtle()
green_turtle.color("green")
green_turtle.penup()
green_turtle.shape("turtle")
green_turtle.goto(-200, -50)

purple_turtle = Turtle()
purple_turtle.color("purple")
purple_turtle.shape("turtle")
purple_turtle.penup()
purple_turtle.goto(-200, -150)

# Begin race
def move_turtles(turtle_list):
    for turtle in turtle_list:
        turtle.forward(random.randint(10, 50))
        if turtle.xcor() >= 180:
            return turtle.pencolor()
    return "no_winner"

finish = False
turtle_list = [red_turtle, blue_turtle, green_turtle, purple_turtle]
while finish == False:
    winner = move_turtles(turtle_list)
    if winner != "no_winner":
        finish = True

# Announce results

print("The winner is: " + str(winner))
if (winner == user_bet):
    print("Congratulations, you win! Enjoy your zinger box.")
else:
    print("Mate you've lost your car, go re-mortgage your home to play more")

screen.exitonclick()