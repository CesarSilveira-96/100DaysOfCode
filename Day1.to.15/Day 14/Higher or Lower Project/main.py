# Importar Art e Random e game_data
import random
from art import logo
from art import vs
from game_data import data

# Definir função de jogo que roda enquanto a pessoa acertar
def higher_lower():
    lista = data
    score = 0
    print(logo)
    game_continue = True
    select_a = random.choice(lista)
    del (lista[lista.index(select_a)])
    while game_continue:
    # Selecionar aleatoriamente um item da lista de game_data como 'A', removê-lo da lista e selecionar outro como 'B' (removê-lo também).

        print(f"Compare A: {select_a["name"]}, {select_a["description"]} from {select_a["country"]}.")
        print(f"{vs}")
        select_b = random.choice(lista)
        del (lista[lista.index(select_b)])
        print(f"And B: {select_b["name"]}, {select_b["description"]} from {select_b["country"]}.\n")
        user_answer = input("Who has more followers? Type 'A' or 'B':\n").lower()
    # Acumular pontos caso acerte e continuar o jogo // encerrar o jogo e mostrar a pontuação caso erre.
        if compare_answer(user_choice=user_answer,alternative_a=select_a,alternative_b=select_b):
            score += 1
            select_a = select_b
            print("\n"*100)
            print(logo)
            print(f"You're right! Current Score: {score}.")
        else:
            game_continue = False
    print("\n"*100)
    print(f"You lost! Your final score is: {score}")


    # Definir função que compara os resultados e determina se o usuário acertou ou errou

def compare_answer (user_choice, alternative_a, alternative_b):
    if user_choice == "a" and alternative_a["follower_count"] > alternative_b["follower_count"]:
        return True
    elif user_choice == "b" and alternative_b["follower_count"] > alternative_a["follower_count"]:
        return True
    else:
        return False



higher_lower()