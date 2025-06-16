from turtle import Turtle

class FinishLine(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.hideturtle()
        self.penup()
        self.goto(x=-300,y=300)
        self.color("white")
        self.pensize(2)
        for n in range(-28,30,2):
            self.pendown()
            self.goto(x=((n*10)-20),y=300)
            self.penup()
            self.goto(x=(n*10),y=300)