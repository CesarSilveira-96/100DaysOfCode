import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=700)
screen.tracer(0)

player1 = Player()
scoreboard = Scoreboard()
cars = CarManager()

screen.listen()
screen.onkeypress(player1.move_up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    cars.check_spawn()  # Tenta criar novos carros
    cars.move()   # Move todos os carros

    if cars.xcor() <= -300:
        cars.restart_position()

    # Cross Finish Line
    if player1.ycor() > 280:
        player1.restart_position()
        cars.increase_speed()
        scoreboard.increase_score()

    # Colision with cars
    for car in cars.all_cars:
        if player1.distance(car) < 40 and (car.ycor() -25) < player1.ycor() < (car.ycor() +25):
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()

#
# import time
# from turtle import Screen
# from player import Player  # Supondo que você tenha um jogador
# from car_manager import CarManager
#
# screen = Screen()
# screen.setup(width=600, height=600)
# screen.tracer(0)
#
# player = Player()
# car_manager = CarManager()
#
# screen.listen()
# screen.onkeypress(player.move_up, "Up")
#
# game_is_on = True
# while game_is_on:
#     time.sleep(0.05)
#     screen.update()
#

#
#     # Verifica colisões (opcional)
#     for car in car_manager.all_cars:
#         if player.distance(car) < 20:
#             game_is_on = False
#             print("Game Over!")
#
# screen.exitonclick()