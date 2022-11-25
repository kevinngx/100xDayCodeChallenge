import pandas as pd
import turtle

# Setup screen
screen = turtle.Screen()
screen.title("Make America Great Again")
usa_map_image = "blank_states_img.gif"
screen.addshape(usa_map_image)
turtle.shape(usa_map_image)

pen = turtle.Turtle()
pen.hideturtle() 
pen.penup()
pen.speed("fastest")

# Extract data from pandas file
data = pd.read_csv("50_states.csv")

# Get answer
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title="Guess a state", prompt="Name another state's name").title()
       
    if answer_state in data.values:
        state = data[data['state'] == answer_state]
        pen.goto(state.x.values[0], state.y.values[0])
        pen.write(state.state.values[0])
        guessed_states.append(answer_state)
    
    if answer_state  == "Exit":
        break

all_states = data.state.to_list()
pd.DataFrame([state for state in all_states if state not in guessed_states]).to_csv("states_to_learn.csv")

screen.exitonclick()

