import colorgram
import turtle as t
import random

def random_color(colors):
    random_color = random.randint(0, len(colors)-1)
    return colors[random_color].rgb

colors = colorgram.extract('painting.jpg', 6)
t.colormode(255)
# random_color(colors)

tim = t.Turtle()
tim.penup()
tim.speed("fastest")

def paint_masterpiece(size):    
    height = -size

    for _ in range(0, size):
        tim.setposition(-size, height)
        for _ in range(0, size):
            tim.dot(20, random_color(colors))
            tim.fd(40)
        height += 40
    
paint_masterpiece(10)

screen = t.Screen()
screen.exitonclick()
