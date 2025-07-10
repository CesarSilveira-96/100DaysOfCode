from turtle import Turtle


class Walls(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.hideturtle()
        self.penup()
        self.goto(x=-320,y=-420)
        self.color("white")
        self.pendown()
        self.goto(x=320,y=-420)
        self.goto(x=320,y=370)
        self.goto(x=-320,y=370)
        self.goto(x=-320,y=-420)
        self.create_bottom_line()

    def create_bottom_line(self):
        self.speed("fastest")
        self.hideturtle()
        self.penup()
        self.goto(x=-310,y=-380)
        self.color("whitesmoke")
        for n in range(-270,370,40):
            self.pendown()
            self.goto(n-20,-380)
            self.penup()
            self.goto(n,-380)
