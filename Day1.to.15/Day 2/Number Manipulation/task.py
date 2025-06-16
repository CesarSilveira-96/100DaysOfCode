bmi = 84 / 1.65 ** 2

print(round(bmi,2)) # Round arredonda números quebrados --> pode colocar número de casas decimais desejado

# resultados acumulados / contagem de pontos

score = 0
print(score)

# Usuário marcou ponto --> Score é 1
score += 1
print(score)

# Usuário marcou ponto --> Score é 2
score += 1
print(score)

# Outras operações cumulativas
# -=
# *=
# /=

#f-string
is_winning = True
age = 18
print(f"The {age} years old athlete is winning with {score} points")