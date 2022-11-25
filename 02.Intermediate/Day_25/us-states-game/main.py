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
        print("Correct")
        state = data[data['state'] == answer_state]
        print(state.values)
        state_name = state.state.values[0]
        x = state.x.values[0]
        y = state.y.values[0]

        pen.goto(x, y)
        pen.write(state_name)
        guessed_states.append(answer_state)
    
    if answer_state  == "Exit":
        break

# States to learn
missing_states = []
all_states = data.state.to_list()
for state in all_states:
    if state not in guessed_states:
        missing_states.append(state)
df_missing_states = pd.DataFrame(missing_states)
df_missing_states.to_csv("states_to_learn.csv")

screen.exitonclick()

