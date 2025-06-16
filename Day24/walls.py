from turtle import Turtle


class Walls(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.hideturtle()
        self.penup()
        self.goto(x=-290,y=-290)
        self.color("white")
        self.pendown()
        self.goto(290,-290)
        self.goto(290,290)
        self.goto(-290,290)
        self.goto(-290,-290)
