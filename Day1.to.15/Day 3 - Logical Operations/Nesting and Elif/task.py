from tokenize import endpats
from typing import final

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?\n"))
    if age < 18:
        print("The ticket costs $7")
    if age >= 18:
        print("The ticket costs $12")
else:
    print("Sorry you have to grow taller before you can ride.")
