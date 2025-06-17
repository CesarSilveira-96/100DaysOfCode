# programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
#                           "Function": "A piece of code that you can easily call over and over again."}
#
# print(programming_dictionary["Bug"])
#
# programming_dictionary["Loop"] =  "The action of doing something over and over again"
# print(programming_dictionary)
#
# empty_dictionary = {}
#
# # Edit an item in a dictionary
#
# programming_dictionary["Bug"] = "A moth in your computer"
# print(programming_dictionary["Bug"])
#
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for name in student_scores:
    student_grades[name]:student_scores[name]
    if student_scores[name] <= 70:
        student_grades[name] = "Fail"
    elif student_scores[name] <= 80:
        student_grades[name] = "Acceptable"
    elif student_scores[name] <= 90:
        student_grades[name] = "Exceeds"
    elif student_scores[name] <= 100:
        student_grades[name] = "Outstanding"

print(student_grades)
# TODO: write code...