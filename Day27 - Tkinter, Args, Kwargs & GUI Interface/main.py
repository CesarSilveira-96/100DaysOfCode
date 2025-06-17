# Tkinter
    # GUI = Graphical User Interface
from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    result_label.config(text=f"{km}")

window = Tk()
window.title("Miles to Kilometer converter")
window.minsize(width=100,height=100)
window.config(padx=40,pady=40)

# Label


miles_label = Label(text= "Miles")
miles_label.grid(column=2, row=0)
miles_label.config(padx=10,pady=10)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)
equal_label.config(padx=10,pady=10)

result_label = Label(text=f"{0}")
result_label.grid(column=1, row=1)
result_label.config(padx=10,pady=10)

km_label = Label(text= "Km")
km_label.grid(column=2, row=1)
km_label.config(padx=10,pady=10)

# Button
# def button_clicked():
#     print("I got clicked")
#     my_label.config(text=f"{inputs.get()}")
button = Button(text= "Calculate", command=miles_to_km)
button.grid(column=1,row=2)
button.config(padx=10,pady=10, borderwidth=5)


# Entry
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)
miles_input.insert(END,"0") # Insert starting text
miles_input.config(borderwidth=5)


#
window.mainloop()