from tkinter.constants import CENTER
from turtle import Turtle
ALLIGNMENT = "center"
FONT = ("Courier", 12,"normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=0,y=290)
        self.color("white")
        self.score = 0
        with open("my_highscore_file.txt") as file:
            self.highscore = int(file.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} | Highscore: {self.highscore}", align=CENTER, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_score(self):
        if self.score > self.highscore:
            with open("my_highscore_file.txt", mode="w") as file:
                file.write(f"{self.score}")
            with open("my_highscore_file.txt") as file:
                self.highscore = int(file.read())
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.color("red")
    #     self.write(arg="GAME OVER", align=CENTER, font=FONT)



