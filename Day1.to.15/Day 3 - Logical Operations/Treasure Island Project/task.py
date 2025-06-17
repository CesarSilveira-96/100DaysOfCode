print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
path = input("Which path do you want to pick?"
             " Type \"Left\" or \"Right\":\n").lower()
if path == "Left":
    lake = input("You ran into a lake. "
                 "Do you want to swim or wait for the boat?\n")
    if lake == "Wait":
        door = input("You've waited for the boat and got across safely. "
                     "There you see 3 doors. Which one do you choose? "
                     "\"Red\", \"Blue\" or \"Yellow?\"\n").lower()
        if door == "Red":
            print("You were burnt by the flames and died. Game Over")
        if door == "Blue":
            print("You got eaten by dangerous beasts and died. Game Over")
        if door == "Yellow":
            print("Congratulations, you've found the treasure and won!!")
        else:
            print("Game Over Loser!")
    else:
        print("You were attacked by sharks. Game Over")
else:
    print("You took the wrong path and fell into a blackhole. Game Over")


# Para imprimir Aspas duplas ou simples em uma string sem que elas sejam interpretadas como uma nova string basta usar \
print('you\'ve selected "X"') # exemplo com apóstrofe dentro de aspas simples
print("selecione \"sim\" ou \"não\"") # exemplo de aspas duplas repetidas