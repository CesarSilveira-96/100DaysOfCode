from turtle import Turtle

MOVE_DISTANCE = 15

class Paddle (Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.speed("fastest")
        self.penup()
        self.goto(position)

    def move_up(self):
        if self.ycor() != 270:
            self.goto(self.xcor(),self.ycor() + MOVE_DISTANCE)

    def move_down(self):
        if self.ycor() != -270:
            self.goto(self.xcor(), self.ycor() - MOVE_DISTANCE)




# class PaddlePc(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.shape("square")
#         self.color("white")
#         self.shapesize(5,1)
#         self.speed("fastest")
#         self.penup()
#         self.goto(X_POSITION_PC,0)
    #     while PC_MOVING:
    #         self.move_up()
    #         self.move_down()
    #
    #
    # def move_up(self):
    #     while self.ycor() != 270:
    #         self.goto(X_POSITION_PC,self.ycor() + MOVE_DISTANCE)
    #
    # def move_down(self):
    #     while self.ycor() != 270:
    #         self.goto(X_POSITION_PC, self.ycor() - MOVE_DISTANCE)

