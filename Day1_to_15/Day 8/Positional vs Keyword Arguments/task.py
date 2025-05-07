# # Functions with input
#
# def greet_with(name, temp):
#     print(f"Hello {name}")
#     print(f"How do you do?")
#     print(f"It's {temp} degrees outside.")
#
# greet_with("Jack Bauer", "50" # positional argument
#
# greet_with(temp=60, name="César") # keyword argument"

def calculate_love_score(name1,name2):
    cont_true = 0
    cont_love = 0
    for num in range(0,len(name1)):
        if name1[num] == "t":
            cont_true += 1
        if name1[num] == "r":
            cont_true += 1
        if name1[num] == "u":
            cont_true += 1
        if name1[num] == "e":
            cont_true += 1
        if name1[num] == "l":
            cont_love += 1
        if name1[num] == "o":
            cont_love += 1
        if name1[num] == "v":
            cont_love += 1
        if name1[num] == "e":
            cont_love += 1
        if name2[num] == "t":
            cont_true += 1
        if name2[num] == "r":
            cont_true += 1
        if name2[num] == "u":
            cont_true += 1
        if name2[num] == "e":
            cont_true += 1
        if name2[num] == "l":
            cont_love += 1
        if name2[num] == "o":
            cont_love += 1
        if name2[num] == "v":
            cont_love += 1
        if name2[num] == "e":
            cont_love += 1
    print (f"{cont_true}{cont_love}")

calculate_love_score("Kanye West", "Kim Kardashian")
