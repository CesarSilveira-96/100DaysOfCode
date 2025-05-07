# Draw a spot painting

import random
# import colorgram
import turtle as tt

tim = tt.Turtle()
# colors = colorgram.extract('hirst_paint.png',30)
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
rgb_colors = [(245, 244, 240), (244, 241, 243), (240, 242, 245), (241, 244, 241), (1, 1, 0), (23, 103, 157), (217, 153, 102), (158, 69, 48), (237, 216, 102), (152, 58, 80), (133, 172, 199), (223, 78, 45), (215, 132, 156), (74, 166, 86), (186, 152, 48), (139, 186, 148), (208, 81, 103), (19, 47, 96), (42, 132, 91), (19, 58, 122), (26, 159, 191), (4, 103, 69), (147, 30, 45), (111, 42, 31), (119, 115, 167), (252, 218, 1), (65, 72, 42), (9, 68, 43), (4, 93, 114), (74, 31, 36)]

tt.colormode(255)

def starting_position():
    tim.up()
    tim.goto(-230,-220)

# def begin_fill():
#     random_rgb = random.choice(rgb_colors)
#     tim.pencolor(random_rgb)
#     tim.color(random_rgb)
#     tim.begin_fill()
#
# def end_fill():
#     tim.end_fill()

# tim.turtlesize(0.01)
tim.hideturtle()
tim.shape("arrow")
tim.speed("fastest")

def draw_line(numer_of_dots, spacing):
    for i in range(numer_of_dots):
        # begin_fill()
        tim.dot(20,random.choice(rgb_colors))
        # end_fill()
        tim.up()
        tim.fd(spacing)
        tim.down()

def go_to_start(number_of_dots,spacing):
    tim.up()
    tim.left(90)
    tim.fd(spacing)
    tim.left(90)
    tim.fd(number_of_dots * spacing)
    tim.setheading(0)
    tim.down()

def draw_art(n_dots,n_spacing,n_lines):
    starting_position()
    for lines in range(n_lines):
        draw_line(n_dots,n_spacing)
        go_to_start(n_dots,n_spacing)

draw_art(10,50,10)


screen = tt.Screen()
screen.exitonclick()