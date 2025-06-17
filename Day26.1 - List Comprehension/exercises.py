# List Comprehension -- new_list = [new_item for item in list] -- works with any sequence (string, range, tuple, list)

# numbers = [1,2,3,4]
# new_list = [item+1 for item in numbers]
# print (new_list)

# name  = "cesar"
# new_list = [letter for letter in name]
# print (new_list)


# new_list = [n*2 for n in range(1,5)]
# print(new_list)

# List comprehension with testing and conditions -- new_list = [new_item for item in list if test/condition]
# names = ["alex","beth","cesar"]
# short_names = [name.upper() for name in names if len(name)<5]
# print(short_names)


# list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
# numbers = [int(n) for n in list_of_strings]
# result = [n for n in numbers if n%2 == 0]
# print(result)

#  DICTIONARY Comprehension -- new_dict = {new_key:new_value for item in list} --> Works with any sequency or dictionary
    # new_dict = {new_key:new_value for (key,value) in dict.items() if test/condition}
# import random
# names = ["alex","beth","cesar", "angela"]
# student_scores = {name:random.randint(0,100) for name in names}
# print(student_scores)

# approved = {name:score for (name,score) in student_scores.items() if int(score) > 50}
# print(approved)

student_dict = {
    "student": ['alex','beth','cesar','angela'],
    'score': [77, 33, 96, 16]
}

# Looping through dictionaries:
# for (key,value) in student_dict.items():
#     print (key)
#     print(value)

import pandas
student_data_frame = pandas.DataFrame(student_dict)

# # Looping through a Data Frame:
# for (key,value) in student_data_frame.items():
#     print (key)
#     print(value)

# #Looping through rows of a DF:
# for (index, row) in student_data_frame.iterrows():
#     if row.student =="cesar":
#         print( row.score)
# Creating dictionaries from DF:
# new_dict = {new_key:new_value for (index,row) in df.iterrows()}