
BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random

current_word = {}
words_dict = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/Top500FrenchWords.csv")
    words_dict = original_data.to_dict(orient="records")
else:
    words_dict = data.to_dict(orient="records")


# ---------------------------- COMMANDS ------------------------------- #
def next_card():
    global current_word, flip_timer
    window.after_cancel(f"{flip_timer}")
    current_word = random.choice(words_dict)
    canvas.itemconfig(language_text, text= f"French", fill= "black")
    canvas.itemconfig(word_text, text= current_word["French"], fill= "black")
    canvas.itemconfig(card_img, image= card_front_img)
    flip_timer = window.after(5000, func=flip_card)

def flip_card():
    global current_word
    canvas.itemconfig(language_text, text= "Portuguese", fill= "white")
    canvas.itemconfig(word_text, text= current_word["Portuguese"], fill= "white")
    canvas.itemconfig(card_img, image= card_back_img)

def is_known():
    words_dict.remove(current_word)
    data = pandas.DataFrame(words_dict)
    data.to_csv("data/words_to_learn.csv", index= False)
    next_card()
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flash Card Game")
window.config(pady=50,padx=50,bg=BACKGROUND_COLOR)

flip_timer = window.after (5000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
card_img = canvas.create_image(400,262,image=card_front_img)
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
right_button.config(image=right_bt_img, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)
















window.mainloop()
