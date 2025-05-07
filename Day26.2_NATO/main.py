# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# #TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index,row) in nato_data.iterrows()}
# print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

                        # Loop using "while True"
# def create_nato_list(word):
#     nato_user_word_list = [nato_dict[letter] for letter in word]
#     print (nato_user_word_list)
#
# while True:
#     user_word = input("Write a word to be encrypted:\n").upper()
#     try:
#         create_nato_list(word=user_word)
#         break
#     except KeyError:
#         print("Sorry, use only letters in the alphabet please.")


                        # Loop inside the function
def create_nato_list():
    user_word = input("Write a word to be encrypted:\n").upper()
    try:
        output_list = [nato_dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry, use only letters in the alphabet please.")
        create_nato_list()
    else:
        print(output_list)

create_nato_list()