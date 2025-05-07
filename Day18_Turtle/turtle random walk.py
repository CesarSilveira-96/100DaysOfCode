# Random color walk
import random

# Atribuindo novo nome ao módulo para facilitar o uso
import turtle as tt

tim = tt.Turtle()

tt.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rand_color = (r,g,b)
    return rand_color


tim.turtlesize(0.01)
tim.pensize(10)
tim.shape("circle")
tim.speed("fastest")



angles = [0,90,180,270]
for i in range(201):
    tim.color(random_color())
    tim.setheading(random.choice(angles))
    tim.fd(20)

screen = tt.Screen()
screen.exitonclick()