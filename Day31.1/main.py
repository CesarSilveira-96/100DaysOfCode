BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random

content = pandas.read_csv("data/Top500FrenchWords.csv")
words_dict = content.to_dict(orient="records")


# ---------------------------- COMMANDS ------------------------------- #
def next_card():
        random_word = random.choice(words_dict)
        canvas.itemconfig(language_text, text= f"French")
        canvas.itemconfig(word_text, text= random_word["French"])


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flash Card Game")
window.config(pady=50,padx=50,bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400,262,image=card_front_img)
language_text = canvas.create_text(400,120,text="French",font=("Arial", 40, "italic"))
word_text = canvas.create_text(400,267,text="WordExample",font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)
next_card()

#Buttons
wrong_bt_img = PhotoImage(file="images/wrong.png")
wrong_button = Button()
wrong_button.config(image=wrong_bt_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_bt_img = PhotoImage(file="images/right.png")
right_button = Button()
right_button.config(image=right_bt_img, highlightthickness=0, command=next_card)
right_button.grid(row=1, column=1)
















window.mainloop()
