from tkinter.constants import CENTER
from turtle import Turtle
ALLIGNMENT = "center"
FONT = ("Courier", 12,"bold")
GAME_OVER_FONT = ("Courier", 22 ,"bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=7,y=330)
        self.color("white")
        self.score_left = 0
        self.score_right = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score:\n {self.score_left}:{self.score_right}", align=CENTER, font=FONT)

    def point_left(self):
        self.score_left += 1
        self.clear()
        self.write(arg=f"Score:\n {self.score_left}:{self.score_right}", align=CENTER, font=FONT)

    def point_right(self):
        self.score_right += 1
        self.clear()
        self.write(arg=f"Score:\n {self.score_left}:{self.score_right}", align=CENTER, font=FONT)


    def game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write(arg="GAME OVER", align=CENTER, font=GAME_OVER_FONT)



