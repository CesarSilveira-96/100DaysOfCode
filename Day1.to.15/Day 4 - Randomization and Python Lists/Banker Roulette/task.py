import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# SOLUÇÃO 1:
print(random.choice(friends))

# SOLUÇÃO 2:
print(friends[random.randint(0,4)])

# SOLUÇÃO 3:

sorteio = random.randint(1,5)

if sorteio == 1:
    print ("Alice")
elif sorteio == 2:
    print ("Bob")
elif sorteio == 3:
    print ("Charlie")
elif sorteio == 4:
    print ("David")
else:
    print("Emanuel")