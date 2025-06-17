import random
from asyncio.streams import FlowControlMixin
from random import choice


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

list = [rock, paper, scissors]

user_choice = input('Choose between "rock", "paper" or "scissors". Type your answer:\n').lower()
pc_choice = random.choice (list)

if user_choice == "rock":
    print (f"you choose:\n{rock}")
    if pc_choice == rock:
        print (f"PC choose:\n{rock}\nIt's a tie.")
    if pc_choice == paper:
        print (f"PC choose:\n{paper}\nYou lost.")
    if pc_choice == scissors:
        print (f"PC choose:\n{scissors}\nYou won!")

if user_choice == "paper":
    print (f"you choose:\n{paper}")
    if pc_choice == rock:
        print (f"PC choose:\n{rock}\nYou won.")
    if pc_choice == paper:
        print (f"PC choose:\n{paper}\nIt's a tie.")
    if pc_choice == scissors:
        print (f"PC choose:\n{scissors}\nYou lost!")

if user_choice == "scissors":
    print (f"you choose:\n{scissors}")
    if pc_choice == rock:
        print (f"PC choose:\n{rock}\nYou lost.")
    if pc_choice == paper:
        print (f"PC choose:\n{paper}\nYou won.")
    if pc_choice == scissors:
        print (f"PC choose:\n{scissors}\nIt's a tie!")

else: "Sorry, could not understand your answer"


# SOLUTION
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# Note: it's worth checking if the user has made a valid choice before the next line of code.
# If the user typed somthing other than 0, 1 or 2 the next line will give you an error.
# You could for example write:

# if user_choice >= 0 and user_choice <= 2:
#     print(game_images[user_choice])

# computer_choice = random.randint(0, 2)
# print("Computer chose:")
# print(game_images[computer_choice])

# if user_choice >= 3 or user_choice < 0:
#     print("You typed an invalid number. You lose!")
# elif user_choice == 0 and computer_choice == 2:
#     print("You win!")
# elif computer_choice == 0 and user_choice == 2:
#     print("You lose!")
# elif computer_choice > user_choice:
#     print("You lose!")
# elif user_choice > computer_choice:
#     print("You win!")
# elif computer_choice == user_choice:
#     print("It's a draw!")
