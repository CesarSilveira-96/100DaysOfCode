import turtle as tt
import pandas

screen = tt.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
tt.shape(image)

# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# tt.onscreenclick(get_mouse_click_coor)
'''Code used to find the locations of each click on the screen (states)'''

# tt.mainloop()
'''Keeps screen open even after click'''

# Pandas
data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()
guessed_states = []


user_state_answer = screen.textinput("U.S. States Game", "Write the name of a U.S. State:").title()

while len(guessed_states) < 50:
    if user_state_answer == "Exit":
        states_to_learn = [state for state in states_list if state not in guessed_states]
        # for state in states_list:
        #     if state not in guessed_states:
        #         states_to_learn.append(state)
        df = pandas.DataFrame(states_to_learn)
        df.to_csv("states_to_learn.csv")
        break

    elif user_state_answer in states_list and user_state_answer not in guessed_states:
        guessed_states.append(user_state_answer)
        t = tt.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data.state == user_state_answer]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(user_state_answer)

    if len(guessed_states) < 50:
        user_state_answer = screen.textinput(f"{len(guessed_states)}/50 States Guessed.", "Write the name of a U.S. State:").title()
    else:
        t = tt.Turtle()
        t.penup()
        t.hideturtle()
        t.goto(0,0)
        t.color("Medium Blue")
        t.write("Congratulations!\nYou Remembered all of the 50 states!",align="Center",font=("Arial",24,"bold"))
        game_continue = False





screen.exitonclick()