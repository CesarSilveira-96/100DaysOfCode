from Menu import MENU
from Menu import resources
machine_working = True
money = 0

def check_money(order):
    transaction_successfull = True
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    total_inserted_money = float((quarters*0.25) + (dimes*0.1) + (nickels*0.05) + (pennies*0.01))
    change = float(total_inserted_money - MENU[order]["cost"])
    if total_inserted_money < MENU[order]["cost"]:
        print("Sorry, not enough money. Your coins were refunded.")
        transaction_successfull = False
    elif total_inserted_money > MENU[order]["cost"]:
        print(f"Here is ${round(float(change),2)} in exchange")

    return transaction_successfull




def check_resources(drink):
    if resources["water"] < MENU[f"{drink}"]["ingredients"]["water"]:
        print("Sorry, there is not enough water for that order.")
        return False
    else:
        if resources["coffee"] < MENU[f"{drink}"]["ingredients"]["coffee"]:
            print("Sorry, there is not enough coffee for that order.")
            return False
        else:
            if "milk" in MENU[f"{drink}"]["ingredients"] and resources["milk"] < MENU[f"{drink}"]["ingredients"]["milk"]:
                print("Sorry, there is not enough milk for that order.")
                return False
            else:
                print(f"{drink} = ${MENU[drink]["cost"]}0. Please insert coins.")
                if check_money(order=drink):
                    return True





while machine_working:
    # global money
    user_choice = input("What would you like? (espresso/latte/cappuccino):\n").lower()
    if user_choice == "report":
        print(f"Water: {resources["water"]}ml\n"
              f"Milk: {resources["milk"]}ml\n"
              f"Coffe: {resources["coffee"]}g\n"
              f"Money: ${float(money)}")
    else:
        if check_resources(drink=user_choice):
                resources["water"] = resources["water"] - MENU[f"{user_choice}"]["ingredients"]["water"]
                resources["coffee"] = resources["coffee"] - MENU[f"{user_choice}"]["ingredients"]["coffee"]
                if "milk" in MENU[f"{user_choice}"]["ingredients"]:
                    resources["milk"] = resources["milk"] - MENU[f"{user_choice}"]["ingredients"]["milk"]
                money += MENU[user_choice]["cost"]