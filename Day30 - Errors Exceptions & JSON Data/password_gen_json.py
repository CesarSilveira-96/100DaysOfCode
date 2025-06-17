import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def password_gen():

    password_input.delete(first=0,last=END)

    nr_letters = randint(8,10)
    nr_symbols = randint(2,4)
    nr_numbers = randint(2,4)

    password_letters =  [choice(letters) for _ in range(nr_letters)]
    password_symbols =  [choice(symbols) for _ in range(nr_symbols)]
    password_numbers =  [choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)
    password = "".join(password_list)
    password_input.insert(0,f"{password}")

    pyperclip.copy(password)

    # COPYING TO CLIPBOARD WITH TKINTER
    # clipboard = Tk()
    # clipboard.withdraw()
    # clipboard.clipboard_clear()
    # clipboard.clipboard_append(password)
    # clipboard.update()  # now it stays on the clipboard after the window is closed
    # clipboard.destroy()



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_to_file():
    website = website_input.get().lower()
    email = email_user_input.get().lower()
    password = password_input.get().lower()
    new_data = {website:
        {
            "email":email,
            "password": password
        }
    }

    if len(website) != 0 and len(email) != 0 and len(password) != 0:
        try:
            with open("password_data.json", "r") as data_file:
                # Tenta carregar dados existentes
                data = json.load(data_file)
        except (FileNotFoundError, json.JSONDecodeError):
            # Arquivo não existe ou está vazio/corrompido
            with open("password_data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updates old data with new data
            data.update(new_data)

            with open("password_data.json", "w") as data_file:
                # Saves updated data
                # noinspection PyTypeChecker
                json.dump(data, data_file, indent=4)

        finally:
            website_input.delete(first=0, last=END)
            password_input.delete(first=0, last=END)
            pyperclip.copy(password)

    else:
        messagebox.showinfo(title="Error", message=f"Website field is empty!")


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search():
    website_entry = website_input.get().lower()

    if len(website_entry) == 0:
        messagebox.showinfo(title="Error", message=f"Website field is empty!")

    else:
        try:
            with open("password_data.json", "r") as data_file:
                data = json.load(data_file)
        except (FileNotFoundError, json.JSONDecodeError):
            messagebox.showinfo(title="Error!", message=f"No data file found!")

        else:
            if website_entry in data:
                email = data[website_entry]["email"]
                password = data[website_entry]["password"]
                email_user_input.delete(first=0, last=END)
                email_user_input.insert(0,f"{email}")
                password_input.delete(first=0, last=END)
                password_input.insert(0,f"{password}")
                messagebox.showinfo(title=website_entry, message=f"🔒\n"
                                                           f"Email: {email}\n"
                                                           f"Password: {password}")
                pyperclip.copy(password)

            else:
                messagebox.showinfo(title="Error!", message=f"No password found for this website.")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(pady=50,padx=50,bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

# Labels
website_label = Label(text="Website:", bg="white")
website_label.grid(row= 1, column= 0)

email_user_label = Label(text="Email/Username:", bg="white")
email_user_label.grid(row= 2, column= 0)

password_label = Label(text="Password:", bg="white")
password_label.grid(row= 3, column= 0)

#Inputs
website_input = Entry()
website_input.config(width=32)
website_input.grid(row=1, column=1, pady=5)
# website_input.insert(END, "0") # Insert starting text

email_user_input = Entry()
email_user_input.insert(0, "cesar1234@email.com")
email_user_input.config(width=50)
email_user_input.grid(row=2, column=1, columnspan=2, pady=5)

password_input = Entry()
password_input.config(width=32)
password_input.grid(row=3, column=1, pady=5)

#Buttons
generate_button = Button()
generate_button.config(text="Generate Password", width=14, command=password_gen)
generate_button.grid(row=3, column=2,pady=5)

add_button = Button()
add_button.config(text="Add", width=43, command=save_to_file)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button()
search_button.config(text="Search", width=14, command=search)
search_button.grid(row=1, column=2)















window.mainloop()