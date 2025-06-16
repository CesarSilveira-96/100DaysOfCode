from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
CAR_SPAWN_CHANCE = 0.10  # x% de chance de gerar um carro a cada frame

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.spawn_chance = CAR_SPAWN_CHANCE
        self.car_speed = STARTING_MOVE_DISTANCE
        self.hideturtle()
        self.penup()
        self.goto(300, -300)


    def create_car(self):
        new_car = Turtle("square")
        new_car.penup()
        new_car.shapesize(stretch_wid=1, stretch_len=3)
        new_car.color(random.choice(COLORS))
        random_y = random.randint(-22, 28) * 10  # Posição Y aleatória
        new_car.goto(300, random_y)
        self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def check_spawn(self):
        if random.random() < self.spawn_chance:  # Probabilidade de spawn
            self.create_car()

    def restart_position(self):
        self.color(random.choice(COLORS))
        self.goto(300,(random.randint(-24,24)*10))

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT

#
# from turtle import Turtle
# import random
#
# COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
# STARTING_MOVE_DISTANCE = 5
# MOVE_INCREMENT = 10
# CAR_SPAWN_CHANCE = 0.02  # 2% de chance de gerar um carro a cada frame
#
# class CarManager:
#     def __init__(self):
#         self.all_cars = []  # Lista para armazenar todos os carros
#         self.car_speed = STARTING_MOVE_DISTANCE
#         self.spawn_chance = CAR_SPAWN_CHANCE
#
#     def create_car(self):
#         """Cria um novo carro em uma posição Y aleatória."""
#         new_car = Turtle("square")
#         new_car.penup()
#         new_car.shapesize(stretch_wid=1, stretch_len=3)
#         new_car.color(random.choice(COLORS))
#         random_y = random.randint(-24, 24) * 10  # Posição Y aleatória
#         new_car.goto(300, random_y)
#         self.all_cars.append(new_car)
#
#     def move_cars(self):
#         """Move todos os carros para a esquerda."""
#         for car in self.all_cars:
#             car.backward(self.car_speed)
#
#     def check_spawn(self):
#         """Verifica se um novo carro deve ser criado (aleatoriamente)."""
#         if random.random() < self.spawn_chance:  # Probabilidade de spawn
#             self.create_car()
#
#     def increase_speed(self):
#         """Aumenta a velocidade dos carros."""
#         self.car_speed += MOVE_INCREMENT




