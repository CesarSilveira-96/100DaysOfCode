# TODOs:
from turtle import Turtle,Screen
from paddles import Paddle
from scoreboard import Scoreboard
from walls import Walls
from ball import Ball
import time

screen = Screen()
screen.setup(width=1200, height=800)
screen.bgcolor("black")
screen.title("Pong Pong")
screen.tracer(0)

walls = Walls()
r_paddle = Paddle((500,0))
l_paddle = Paddle((-500,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()


    if ball.xcor() > 490:
        scoreboard.point_left()
        ball.stop()

    elif ball.xcor() < -490:
        scoreboard.point_right()
        ball.stop()

    elif ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce_wall()

    elif (ball.distance(l_paddle) < 60 or ball.distance(r_paddle) < 60) and (ball.xcor() >= 480 or ball.xcor() <= -480):
        ball.bounce_paddle()

    # if scoreboard.score_left == 3 and scoreboard.score_right < 3:
    #     ball.change_speed()
    #
    # elif scoreboard.score_left < 3 and scoreboard.score_right == 3:
    #     ball.change_speed()

    if scoreboard.score_left == 5 or scoreboard.score_right == 5:
        scoreboard.game_over()
        game_is_on = False



screen.exitonclick()