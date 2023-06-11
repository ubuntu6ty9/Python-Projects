import turtle
from scoreboard import Scoreboard
import pandas as pd

# screen set-up
screen = turtle.Screen()
screen.title("US States Game")
screen.setup(width=730, height=600)
screen.bgcolor("#F1DAA0")
screen.tracer(0)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# initialize scoreboard to track user score
scoreboard = Scoreboard()

screen.update()

# read csv file with pandas
states_df = pd.read_csv("50_states.csv")

# extract all available states into a list
states_list = states_df.state.to_list()


def check_answer(user_input):
    if user_input in states_list:
        state = states_df[states_df.state == user_input]
        x_cor = state.x.iloc[0]
        y_cor = state.y.iloc[0]
        turtle.goto(x=x_cor, y=y_cor)
        turtle.color("red")
        turtle.write(user_input, align="center", font=("Lato", 12, "normal"))
        scoreboard.update_score()
        states_list.remove(user_input)
    elif user_input == "Quit":
        quit()


game_is_on = True

while game_is_on:
    user_input = screen.textinput(title="Guess a state", prompt="Guess a state").title()
    check_answer(user_input=user_input)

turtle.mainloop()
