enemies = 1 #Global Scope disponível para qualquer nível do arquivo


def increase_enemies():
    enemies = 2 # loca scope - só está defionido dentro da função
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

# Namespace

player_health = 10

def game():
    def drink_potion():
        potion_strenght = 2
        print(player_health + potion_strenght)
    drink_potion()

print(player_health)