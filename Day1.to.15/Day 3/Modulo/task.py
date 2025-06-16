# Resto de uma divisão (Ramainder) --> %
print (str(6 % 2)) # a divisão da 3 exato, portanto o resto é 0
print (str(6 % 4)) # a divisão da 1 com resto 2
print (str(6 % 5)) # a divisão da 1 com resto 1

# Pause 1
print(str(10 % 3)) # resto = 1

#Pause 2
number_user = int(input("Select a number from 1 to 10\n"))
if (number_user % 2) == 0:
    print("Even")
else:
    print("Odd")
