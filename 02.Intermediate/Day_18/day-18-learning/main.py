from turtle import Turtle, Screen
import random

def randomize_color():
    R = random.random()
    B = random.random()
    G = random.random()
    tim.pencolor(R, G, B)

tim = Turtle()

# Turtle format
tim.shape("turtle")

# Activity 1 - Draw a square
# for i in range(0, 4):
#     tim.right(90)
#     tim.forward(100)    

# Activity 2 - Dotted line
# for i in range(0, 20):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


# Activity 3 - Increasig Shapes
# sides = 3
# for i in range(sides, 10):
#     for t in range(0, sides):
#         angle = 360/sides
#         tim.forward(100)
#         tim.right(angle)
#     sides += 1
#     randomize_color()

# Activity 4 - Random Walk
# tim.width(10)
# tim.pen(speed=10)
# for i in range(0, 100):
#     tim.right(random.choice([90, 180, 270, 360]))
#     tim.forward(50)
#     randomize_color()

# Activity 5 - Spirograph
def draw_spirograph(size_of_gap):
    # angle = 0
    size = 10
    for _ in range(int(720/size_of_gap)):
        tim.circle(size)
        tim.left(size_of_gap)
        # angle += size_of_gap
        randomize_color()
        size += 2
        


tim.speed("fastest")
size_of_gap = 5
draw_spirograph(size_of_gap)

screen = Screen()
screen.exitonclick()