# Modifying Global Scope

enemies = 1


# def increase_enemies():
#     global enemies
#     enemies += 1
#     print(f"enemies inside function: {enemies}")

def increase_enemies(enemy):

    print(f"enemies inside function: {enemies}")
    return enemy + 1

enemies = increase_enemies(enemies)
print(f"enemies outside function: {enemies}")


# def divisores(num):
#     for i in range(1, num//2+1):
#         if num % i == 0:
#             yield i
#     yield num
#
# def is_prime(num):
#     if len(list(divisores(num))) > 2:
#         print (False)
#     else:
#         print (True)
#
# number = int(input("Choose a number:\n"))
# is_prime(number)