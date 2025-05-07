from turtle import Turtle


class Walls(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.hideturtle()
        self.penup()
        self.goto(x=-540,y=-320)
        self.color("white")
        self.pendown()
        self.goto(x=540,y=-320)
        self.goto(x=540,y=320)
        self.goto(x=-540,y=320)
        self.goto(x=-540,y=-320)
        self.create_middle_line()
        self.create_left_line()
        self.create_right_line()

    def create_middle_line(self):
        self.speed("fastest")
        self.hideturtle()
        self.penup()
        self.goto(x=0,y=-310)
        self.color("whitesmoke")
        for n in range(-270,370,40):
            self.pendown()
            self.goto(0,n-20)
            self.penup()
            self.goto(0,n)

    def create_left_line(self):
        self.speed("fastest")
        self.hideturtle()
        self.penup()
        self.goto(x=-490,y=-310)
        self.color("whitesmoke")
        for n in range(-270,370,40):
            self.pendown()
            self.goto(-490,n-20)
            self.penup()
            self.goto(-490,n)

    def create_right_line(self):
        self.speed("fastest")
        self.hideturtle()
        self.penup()
        self.goto(x=490,y=-310)
        self.color("whitesmoke")
        for n in range(-270,370,40):
            self.pendown()
            self.goto(490,n-20)
            self.penup()
            self.goto(490,n)


