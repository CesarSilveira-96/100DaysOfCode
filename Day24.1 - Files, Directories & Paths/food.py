from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("white")
        self.speed("fastest")
        self.generate_food()

    def generate_food(self):
        random_x = (random.randint(0, 26) * 20) - 260
        random_y = (random.randint(0, 26) * 20) - 260
        self.goto(random_x,random_y)













        # self.create_food()


    # def create_food(self):
    #     food = Turtle("square",visible=False)
    #     food.shapesize(1,1,1.0)
    #     food.penup()
    #     food.color("white","white")
    #     random_x_position = (random.randint(0, 28) * 20) - 280
    #     random_y_position = (random.randint(0, 28) * 20) - 280
    #     food.setpos(x=random_x_position,y=random_y_position)
    #     food.showturtle()