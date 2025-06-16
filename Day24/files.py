# with open ("my_highscore_file.txt") as file:
#     content = file.read()
#     print(content)


with open("my_highscore_file.txt", mode="w") as file: # 'mode' padrão é "r" (read only). "w" substitui o texto e "a" (append) adiciona texto
    file.write("2")