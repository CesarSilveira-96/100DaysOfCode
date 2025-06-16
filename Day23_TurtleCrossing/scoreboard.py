from tkinter.constants import CENTER
from turtle import Turtle

ALLIGNMENT = "center"
FONT = ("Courier", 12, "normal")
GAME_OVER_FONT = ("Courier", 20, "BOLD")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=0,y=330)
        self.color("grey")
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Score: {self.score}", align=CENTER, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,310)
        self.color("red")
        self.write(arg="GAME OVER", align=CENTER, font=FONT)