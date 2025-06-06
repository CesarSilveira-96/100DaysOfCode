from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

# w = forward
# s = backwards
# a = counter-clockwise
# d = clockwise

def move_forwards():
    tim.fd(10)

def move_backwards():
    tim.backward(10)

def turn_counter_clockwise():
    tim.left(10)

def turn_clockwise():
    tim.right(10)

def clear_screen():
    tim.clear()
    tim.up()
    tim.home()
    tim.down()

screen.listen()
screen.onkey(fun=move_forwards, key="w") # function as input -- pass without ()
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=turn_clockwise, key="d")
screen.onkey(fun=turn_counter_clockwise, key="a")
screen.onkey(fun=clear_screen, key="c")

screen.exitonclick()