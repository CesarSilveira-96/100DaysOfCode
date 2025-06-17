from turtle import Turtle


class Ball (Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(.5,.5)
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.move_speed =0.05

    def move(self):
        new_X = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_X,new_y)

    def bounce_wall(self):
        self.y_move *= -1
        self.move_speed *= 0.9

    def bounce_paddle(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def stop(self):
        self.goto(0,0)
        self.x_move *= -1
        self.y_move *= -1
        self.move_speed = 0.05
