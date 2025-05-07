from turtle import Screen
from walls import Walls
from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=640, height=640)
screen.bgcolor("black")
screen.title("Snaky the Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
walls = Walls()

def close_screen():
    screen.bye()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left_move, "Left")
screen.onkey(snake.right_move, "Right")
screen.onkey(close_screen,"Escape")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        scoreboard.update_scoreboard()
        scoreboard.increase_score()
        snake.extend()
        food.generate_food()

    if snake.head.xcor() >= 290 or snake.head.xcor() <= -290 or snake.head.ycor() >= 290 or snake.head.ycor() <= -290:
        snake.reset_snake()
        scoreboard.reset_score()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            snake.reset_snake()
            scoreboard.reset_score()


screen.exitonclick()



