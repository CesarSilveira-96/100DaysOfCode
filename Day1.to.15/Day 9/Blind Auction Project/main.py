# TODO-1: Ask the user for input
from art import logo
print(logo)

auction_open = True
auction_dictionary = { }

while auction_open:
    user_name = input("Write your name:\n")
    user_bid = int(input("Whats the value of your Bid?\n"))
    auction_dictionary[str(user_name)] = user_bid
    more_bids = input("Do you want to add new bids? Type 'Y' or 'N':\n").upper()
    if more_bids == "Y":
        auction_open = True
        print("\n" * 1000)
    else:
        auction_open = False

def winning_bid(bids):
    highest_bid = 0
    auction_winner = ""
    for name in bids:
        if bids[name] > highest_bid:
            highest_bid = bids[name]
            auction_winner=f"{name}"
    print(f"\nThe highest bidder was {auction_winner}, with a bid worth of {bids[auction_winner]}$!\nCongratulations!")
winning_bid(auction_dictionary)

# OU usar a max() function para encontrar qual chave do dicionário tem o maior valor
# print(max(auction_dictionary, keys=auctiondictionary.get))


# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
# print("\n" * 100)

