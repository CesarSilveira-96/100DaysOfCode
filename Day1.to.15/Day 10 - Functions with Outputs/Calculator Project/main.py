# >>>>>>>> SOLUÇÃO 1 - ORIGINAL - FUNCIONANDO!!!!!!!!!!!!!!!!!! <<<<<<<

# def add(n1, n2):
#     print(f"{n1} + {n2} = {n1 + n2}")
#     return n1 + n2
# def sub(n1,n2):
#     print(f"{n1} - {n2} = {n1 - n2}")
#     return n1 - n2
# def mult(n1,n2):
#     print(f"{n1} * {n2} = {n1 * n2}")
#     return n1 * n2
# def div(n1,n2):
#     print(f"{n1} / {n2} = {n1 / n2}")
#     return n1 / n2
#
# continue_calculator = True
#
# while continue_calculator:
#     from art import logo
#     print(logo)
#     user_number = float(input("Welcome to César's Calculator!\n"
#                               "What's the first number?\n"))
#     same_number = True
#     while same_number:
#         op_choice = input("\nChoose one of the following operations:\n"
#                           "+\n"
#                           "-\n"
#                           "x\n"
#                           "/\n")
#         second_number = float(input("\nWhat's the second number?\n"))
#
#         if op_choice == "+":
#             user_number = add(user_number,second_number)
#         elif op_choice == "-":
#             user_number = sub(user_number,second_number)
#         elif op_choice == "x":
#             user_number = mult(user_number,second_number)
#         elif op_choice == "/":
#             user_number = div(user_number,second_number)
#         else:
#             continue_calculator = False
#             print("\nYou did not choose a valid operation.\n")
#
#         new_number = input(f"\nType 'Y' to use {user_number} for your next calculation. Type 'N' to use a new number:\n").lower()
#         if new_number == "n":
#             same_number = False
#             print("\n"*100)
#

#>>>>>>>>>>> SOLUÇÃO OTIMIZADA <<<<<<<<<<<<

def add(n1, n2):
    return n1 + n2
def sub(n1,n2):
    return n1 - n2
def mult(n1,n2):
    return n1 * n2
def div(n1,n2):
    return n1 / n2

operations = {
    "+":add,
    "-":sub,
    "x":mult,
    "/":div
}

continue_calculator = True

def calculator():
    from art import logo
    print(logo)
    num_1 = float(input("Welcome to César's Calculator!\n"
                              "What's the first number?\n"))
    same_number = True
    while same_number:
        for symbol in operations:
            print(symbol)
        op_choice = input("Choose one of the operations above:\n")
        num_2 = float(input("\nWhat's the second number?\n"))
        answer = operations[op_choice](num_1,num_2)
        print(f"{num_1} {op_choice} {num_2} = {answer}")

        new_number = input(f"\nType 'Y' to use {answer} for your next calculation. Type 'N' to use a new number:\n").lower()
        if new_number == "y":
            num_1 = answer
        else:
            same_number = False
            print("\n"*100)
            calculator()

calculator()