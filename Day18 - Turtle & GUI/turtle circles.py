# Draw a spirograph

import random
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
tim.shape("circle")
tim.speed("fastest")

def draw_spirograph(size_of_gap):
    for i in range (int(360 / size_of_gap)):
        tim.pencolor(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(random.randint(5,10))

screen = tt.Screen()
screen.exitonclick()