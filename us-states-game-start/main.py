import turtle
import pandas
screen=turtle.Screen()
screen.title("U.S. States Game")
image="blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)


data=pandas.read_csv("50_states.csv")
all_states= data.state.to_list()
game_is_on=True
while game_is_on:
    answer_state = screen.textinput(title="Guess the state", prompt="Name a State").title()
    if answer_state in all_states:
        state_data=data[data["state"]==answer_state]
        t=turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.color("black")
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)




screen.exitonclick()

