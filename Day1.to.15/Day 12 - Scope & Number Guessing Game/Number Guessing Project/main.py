import random
lista = list(range(1, 101))

from art import logo
print(logo)

game_continue = True

def guessing_game(attempts):
    global lista
    global game_continue
    num_to_guess = random.choice(lista)
    while attempts > 0:
        user_number = int(input("Choose a number:\n"))
        if user_number == num_to_guess:
            print(f"You Got It! The chosen number was {user_number}.")
            attempts = -1
        elif user_number > num_to_guess:
            attempts -= 1
            if attempts == 0:
                print(f"Too High! You've got no attempts left.")
            else:
                print(f"Too High! You've got {attempts} attempt left. Try Again!")
        elif user_number < num_to_guess:
            attempts -= 1
            if attempts == 0:
                print(f"Too Low! You've got no attempts left.")
            else:
                print(f"Too Low! You've got {attempts} attempt left. Try Again!")
    if attempts == 0:
        print(f"You lost :(\n"
              f"The chosen number was {num_to_guess}\n")

    keep_playing = input("Do you want to play again? Type 'y' or 'n':\n").lower()
    if keep_playing == "n":
        game_continue = False
    else:
        game_continue = True
    print("\n" * 1000)
    return game_continue

while game_continue:
    print("Welcome to the Guessing Game!"
          "\nI'm thinking of a number between 1 and 100.")
    choose_difficulty = input("Choose a difficulty. Type 'easy' or 'hard':\n").lower()

    if choose_difficulty == "easy":
        print("You have 10 Attempts.\n")
        guessing_game(attempts=10)
    else:
        print("You have 10 Attempts.\n")
        guessing_game(attempts=5)