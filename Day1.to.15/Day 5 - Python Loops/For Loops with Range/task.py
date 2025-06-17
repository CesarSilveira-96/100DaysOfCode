# Range Function

# for number in range(1,11):
# Range vai do primeiro até o penúltimo número (neste caso iria de 1 a 10 sem incluir o 11)
#     print(number)

# for number in range(1,11,3):
# o terceiro elemento dentro dos parênteses (no caso o 3) determina a "cadência" da leitura dos números.
# neste caso, range lerá de 3 em 3 iniciando pelo 1 e terminando em 10 (1, 4, 7, 10)

#GAUSS CHALLENGE
sum = 0
for number in range (1,101):
    sum += number

print(sum)
