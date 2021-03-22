import turtle
import pandas as pd
ALIGNMENT = "center"
FONT = ("Arial", 12, "bold")

states_df = pd.read_csv("50_states.csv")
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
pointer = turtle.Turtle()
pointer.penup()
pointer.hideturtle()


guesses = []
while len(guesses) != 50:
    answer_state = screen.textinput(title=f"{len(guesses)}/50 States Correct", prompt="What's another state's name?").title()
    
    if answer_state == "Exit":
        break

    #Check if guess is among 50 states
    if answer_state in states_df.values and answer_state not in guesses:
        x = int(states_df[states_df.state == answer_state]["x"])
        y = int(states_df[states_df.state == answer_state]["y"])
        pointer.goto(x,y)
        pointer.write(f"{answer_state}", False, align=ALIGNMENT, font=FONT)
        guesses.append(answer_state)

#States to learn.csv
states_to_learn_df = states_df.loc[~states_df.state.isin(guesses)].set_index("state").reset_index()
states_to_learn_df.state.to_csv("states_to_learn.csv")