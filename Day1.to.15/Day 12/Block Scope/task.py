# Não existe Block scope em Python!!
from types import new_class

game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

def create_enemie():
    new_enemy = ""
    if game_level < 5:
        new_enemy = enemies [0]
    print(new_enemy)

create_enemie()