import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# função Blackjack
game_continue = True

def blackjack(hand1,hand2,score1,score2):
    print ("\n"*1000)
    print(logo)
    draw_card = True
    for num in range(0, 2):
        random_card_user = random.choice(cards)
        hand1.append(random_card_user)
        score1 += random_card_user
    print(f"Your hand is: {hand1}. Score of {score1}.")
    for num in range(0, 2):
        random_card_dealer = random.choice(cards)
        hand2.append(random_card_dealer)
        score2 += random_card_dealer
    if score2 == 21:
        print(f"The dealer's hand is: {hand2}.")
        print("You Lose. Dealer have a Blackjack")
        draw_card = False
    elif score1 == 21:
        print(f"The dealer's hand is: {hand2}.")
        print("You Won. You have a Blackjack")
        draw_card = False
    else:
        print(f"Dealer's hand is: [{hand2[0]}]")
        while draw_card:
            want_draw = input("Type 'y' to get another card, type 'n' to pass:\n")
            if want_draw == "y":
                random_card_user = random.choice(cards)
                hand1.append(random_card_user)
                score1 += random_card_user
                if score1 > 21 and not 11 in hand1:
                    draw_card = False
                    print(f"Your hand is: {hand1}. Final Score of {score1}.")
                    print(f"The dealer's hand is: [{hand2[0]}]. Final Score of {hand2[0]}.")
                    print("You lost. You Went Over")
                elif score1 > 21 and 11 in hand1:
                    del (hand1[hand1.index(11)])
                    hand1.append(1)
                    score1 = score1 - 10
                    print(f"Your hand is: {hand1}. Your Score is {score1}.")
                    print(f"The dealer's hand is: {hand2[0]}.")
                else:
                    print(f"Your hand is: {hand1}. Your Score is {score1}.")
                    print(f"The dealer's hand is: [{hand2[0]}].")
            else:
                print(f"Your hand is: {hand1}. Your Final Score is {score1}.")
                while score2 <= 16:
                    random_card_dealer = random.choice(cards)
                    hand2.append(random_card_dealer)
                    score2 += random_card_dealer
                    if score2 > 21 and 11 in hand2:
                        del (hand2[hand2.index(11)])
                        hand2.append(1)
                        score2 = score2 - 10
                print(f"The dealer's hand is: {hand2}. Dealers Final Score is {score2}")
                if score2 > 21:
                    print ("You Won! The Dealer went over.")
                    draw_card = False
                elif score2 > score1:
                    print("You Lost")
                    draw_card = False
                elif score2 == score1:
                    print("It's a Draw!")
                    draw_card = False
                else:
                    print("You Won!")
                    draw_card = False

while game_continue:
    hand_user = []
    hand_dealer = []
    score_user = 0
    score_dealer = 0
    game_start = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n':\n")
    if game_start == "y":
        blackjack(hand_user,hand_dealer,score_user,score_dealer)
    else:
        game_continue = False
