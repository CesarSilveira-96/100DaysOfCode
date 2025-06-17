from tkinter import *
import requests
import random

response = requests.get(url= "https://dummyjson.com/quotes")
response.raise_for_status()
data = response.json()

def get_quote():
    random_number = random.randint(1,30)
    canvas.itemconfig(quote_text, text= f"{data["quotes"][random_number]["quote"]}")
    #Write your code here.


window = Tk()
window.title("Einstein Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Einstein Quote Goes HERE", width=250, font=("Arial", 15, "bold"), fill="white")
canvas.grid(row=0, column=0)

einstein_img = PhotoImage(file="Einstein.png")
einstein_button = Button(image=einstein_img, highlightthickness=0, command=get_quote)
einstein_button.grid(row=1, column=0)



window.mainloop()