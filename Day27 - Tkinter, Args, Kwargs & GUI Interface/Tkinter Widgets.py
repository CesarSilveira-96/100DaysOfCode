# Tkinter
    # GUI = Graphical User Interface
from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500,height=300)

# Label

my_label = Label(text= "I am a Label", font=("Arial", 24, "bold"))
my_label.pack()  # --> generic placing, packs so that everithing fits
# my_label.place(x=100,y=100) --> Specific positions
# my_label.grid() --> grid positioning with x and y coordinates

my_label["text"] = "New Text"
my_label.config(text="NewText")

# Button
def button_clicked():
    print("I got clicked")
    my_label.config(text=f"{inputs.get()}")

button = Button(text= "click me", command=button_clicked)
button.pack()

# Entry

inputs = Entry(width=10)
inputs.pack()
inputs.insert(END,"Write here") # Insert starting text


# Text
text_box = Text(width=40, height=5, borderwidth=10)
text_box.focus() # Puts cursor in textbox
text_box.insert(END,"Example of multi-line text")
print(text_box.get("1.0",END)) #gets current value in textbox at line 1, character 0
text_box.pack()

# Spinbox
def spin_box_used():
    # gets current value in spinbox.
    print(spin_box.get())
spin_box = Spinbox(highlightcolor="green", width=5, values=("1","2","3","4","5"), command=spin_box_used)
spin_box.pack()

# Scale
def scale_used(value):
    print(value)
scales = Scale(from_=1, to=100, command=scale_used)
scales.pack()

# Checkbutton

def checkbutton_used():
    print(checked_state.get())
checked_state = IntVar()
check_button = Checkbutton(text="Is on?",variable=checked_state,command=checkbutton_used)
checked_state.get()
check_button.pack()

# Radiobutton
def radio_used():
    print(radio_state.get())
radio_state = IntVar()
radio_button1 = Radiobutton(text="Option 1",value= 1, variable=radio_state,command=radio_used)
radio_button2 = Radiobutton(text="Option 2",value= 2, variable=radio_state,command=radio_used)
radio_button1.pack()
radio_button2.pack()


# Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(list_box.get(list_box.curselection()))
list_box = Listbox(height=4)
fruits = ["apple", "orange", "strawberry", "pineapple"]
for item in fruits:
    list_box.insert(fruits.index(item),item)
list_box.bind("<<ListboxSelect>>", listbox_used)
list_box.pack()




#
window.mainloop()