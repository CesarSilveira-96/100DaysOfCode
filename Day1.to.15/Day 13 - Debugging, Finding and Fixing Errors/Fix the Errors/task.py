try:
    age = int(input("How old are you?"))
except ValueError:
    print("Your answer must be numbers only (ex.: 15). Try again.")
    age = int(input("How old are you?"))

if age > 18:
    print(f"You can drive at age {age}.")
