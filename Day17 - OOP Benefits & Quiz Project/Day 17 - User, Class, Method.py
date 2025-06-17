# # class User:
#     # pass # usar "pass" para deixar uma função ou classe sem preenchimento (temporariamente)
#          # elimina erros e permite que o código rode
#
# # Criando Objetos sem atributos
# # user_1 = User()
#
# # Criando atributos 1 a 1
# # user_1.id = "001"
# # user_1.name = "Gojira"
# #
# # user_2 = User()
# # user_2.id = "002"
# # user_2.name = "Jack"
#
# # print(f"Hello, {user_1.name}")
#
# # Criando uma Class
# class User:
#     def __init__(self,user_id,user_name): #__init__ = creator ou initializer que ajuda a definir atributos de maneira mais rápida para vários objetos
#         self.id = user_id
#         self.name = user_name
#         self.followers = 0
#         self.following = 0
# # Criando Métodos
#     def follow(self,user):
#         user.followers += 1
#         self.following += 1
#
# # Criando objetos com atributos a partir de um __init__
#
# user_1 = User("001","Gojira")
# user_2 = User("002","Kongo")
#
# print(f"{user_1.name} x {user_2.name}")
# print(f"{user_1.following}")
# print(f"{user_2.followers}")
#
# # User.follow(user_1,user_2) OU
# user_1.follow(user_2)
#
# print(f"{user_1.following}")
# print(f"{user_2.followers}")





