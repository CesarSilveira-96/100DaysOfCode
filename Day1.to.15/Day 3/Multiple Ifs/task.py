print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Child tickets are $5")
        bill += 5
    elif age <= 18:
        print("Adolescent tickets are $7")
        bill += 7
    else:
        print("Adult tickets are $12$")
        bill += 12

    wants_photo = input ("Do you want to have a photo of your ride? Yes or No?\n")
    if wants_photo == "Yes":
    # add$3 to the bill
        bill += 3
        print(f"Your bill is ${bill}")
    else:
        print(f"Your bill is ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
