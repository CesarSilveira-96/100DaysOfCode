from tkinter import *
import math


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    global reps

    window.after_cancel(f"{timer}")
    canvas.itemconfig(timer_text, text= f"00:00")
    check_label.config(text="")
    title_label.config(text="Timer")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps

    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8  == 0:
        countdown(long_break_sec)
        title_label.config(text="✌Break✌", fg=YELLOW)
    elif reps % 2  == 0:
        countdown(short_break_sec)
        title_label.config(text="✌Break✌", fg=PINK)
    else:
        countdown(work_sec)
        title_label.config(text="WORK", fg=RED)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(seconds):
    global reps


    count_min = math.floor(seconds / 60)
    count_sec = seconds % 60
    if count_sec < 10:
        count_sec=f"0{count_sec}"

    if seconds > 0:
        global timer
        canvas.itemconfig(timer_text, text= f"{count_min}:{count_sec}")
        timer = window.after(1, countdown, seconds - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for n in range(work_sessions):
            mark += "✔"
            check_label.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("César's Pomodoro Timer")
window.minsize(width=300,height=200)
window.config(padx=50,pady=50, bg=GREEN)


canvas = Canvas(width=300, height=300, bg=GREEN, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(150,150,image=tomato_img)
timer_text = canvas.create_text(150,170,text="00:00", fill="white", font=(FONT_NAME,30,"bold"))
canvas.grid(row= 1, column= 1)

# Labels
check_label = Label(fg= RED, bg= GREEN, font=(FONT_NAME,15), justify="center")
check_label.grid(row= 3, column= 1)


title_label = Label(text="Timer", bg=GREEN, fg=RED, font=(FONT_NAME,30, "bold"), justify="center")
title_label.grid(row= 0, column= 1)

# Buttons
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row= 2, column= 0)

reset_button = Button(text="Reset",highlightthickness=0, command=timer_reset)
reset_button.grid(row= 2, column= 2)




window.mainloop()
