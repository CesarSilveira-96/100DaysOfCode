import random
from turtle import Turtle,Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "blue", "yellow","green","purple","pink","brown"]
positions = [180,120,60,0,-60,-120,-180]
user_bet = screen.textinput(title="Make your bet!",prompt="Which turtle will win the race? Type a color:")
turtles = []

for turtle_index in range(0,7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y = positions[turtle_index])
    turtles.append(new_turtle)

# def race():
if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 220:
            is_race_on = False
            winner = turtle.pencolor()
            if user_bet == winner:
                print(f"Congratulations, the {winner} turtle won the race!")
            else:
                print(f"You lost. The winner was the {winner} turtle.")

        else:
            ran_distance = random.randint(0, 10)
            turtle.forward(ran_distance)




screen.exitonclick()