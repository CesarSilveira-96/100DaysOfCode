def format_name(f_name, l_name):

    if f_name =="" or l_name == ":":
        return f"\nNo names were found."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"
    print("this string")

print(format_name(input("Write your first name:"), input("Write your last name:")))

