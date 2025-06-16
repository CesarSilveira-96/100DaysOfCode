print("My age: " + str(12))

# Basic operations --> soma (+), sub (-), mult (*), div (/ e //) e sqr (**)
print(123 + 456)
print(7 - 3)
print(3 * 2) # Multiplicação
print(6 / 3) # Resultado da divisão como float
print(5 // 3) # Resultado da divisão como int (cuidado com divisões não exatas)
print(5 ** 3) # Eleva a potência equivalente ao segundo número

# Nível de prioridade entre operações PEMDAS (Parentheses, Exponents, Multiplication/Division, Addition/Subtraction)
# ()
# **
# * OR /
# + OR -

height = 1.65
weight = 84

# Write your code here.
# Calculate the bmi using weight and height.
bmi = weight/(height*height)

print(bmi)

print(round(bmi,2)) # Round arredonda números quebrados --> pode colocar número de casas decimais desejado