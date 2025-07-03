from tkinter import *
from tkinter import messagebox, PhotoImage, ttk, simpledialog
import json
import re


# >>>>>>>>>> Constants and Globals <<<<<<<<<<
SCOREBOARD_FILE = "scoreboard.json"
# --- UI Constants ---
BG_COLOR = "#2E3440"  # Nord Dark
SECONDARY_BG = "#3B4252"
FG_COLOR = "#D8DEE9"  # Nord Light
ACCENT_COLOR = "#88C0D0"  # Nord Frost
ERROR_COLOR = "#BF616A"  # Nord Red

FONT_TITLE = ("Segoe UI", 22, "bold")
FONT_DESC = ("Segoe UI", 10)
FONT_LABEL = ("Segoe UI", 10, "bold")
FONT_GUIDE = ("Segoe UI", 10, "italic")

TIME_LIMIT = 30
timer_id = None
timer_running = False
    typing_box.config(state="normal")
    typing_box.delete("1.0", END)


def check_spelling(event=None):
    """Highlights incorrect words in real-time as the user types."""
    # This function is called on every key release. We also call start_timer
    # to ensure it starts even if the <KeyPress> event were missed.
    # The guard inside start_timer() prevents it from running more than once.
    start_timer()

    # Remove all previous error highlights to re-evaluate the text
    typing_box.tag_remove("error", "1.0", END)

    content = typing_box.get("1.0", "end-1c")
    if not content.strip():
        return

    # Use regex to find all words (sequences of non-space characters).
    # This is robust and handles multiple spaces or newlines correctly.
    for match in re.finditer(r'\S+', content):
        user_word = match.group(0)
        start_char_index = match.start()

        # Determine the word's position in the sequence of typed words
        word_list_index = len(content[:start_char_index].split())

        # Check if the typed word is correct
        is_correct = word_list_index < len(words_list) and user_word == words_list[word_list_index]

        if not is_correct:
            tk_start_index = f"1.0+{start_char_index}c"
            tk_end_index = f"1.0+{match.end()}c"
            typing_box.tag_add("error", tk_start_index, tk_end_index)

def save_scores():
    """Saves the current scoreboard to a JSON file."""
    scores = []
root = Tk()
root.title("Typing Speed Tester")
root.geometry("800x600")
root.resizable(True, True)
root.configure(bg=BG_COLOR)
root.minsize(800, 600)

# >>>>>> Style Configuration (ttk) <<<<<<
style = ttk.Style(root)
style.theme_use("clam")

# Style for the Treeview (Scoreboard)
style.configure("TTreeview",
                background=SECONDARY_BG,
                foreground=FG_COLOR,
                fieldbackground=SECONDARY_BG,
                borderwidth=0,
                rowheight=25)
style.map('TTreeview', background=[('selected', ACCENT_COLOR)])
style.configure("TTreeview.Heading",
                background=BG_COLOR,
                foreground=FG_COLOR,
                font=FONT_LABEL,
                padding=(10, 5))
style.layout("TTreeview", [('Treeview.treearea', {'sticky': 'nswe'})]) # Remove borders

# Style for the Button
style.configure("TButton",
                background=ACCENT_COLOR,
                foreground=BG_COLOR,
                font=FONT_LABEL,
                padding=10,
                borderwidth=0)
style.map("TButton",
          background=[('active', FG_COLOR)],
          foreground=[('active', BG_COLOR)])

# >>>>>> Frames <<<<<<
left_frame = Frame(root, bg=BG_COLOR, padx=20, pady=20)
left_frame.pack(side="left", fill="both", expand=True)

right_frame = Frame(root, bg=SECONDARY_BG, padx=20, pady=20)
right_frame.pack(side="right", fill="y")

# >>>>>> Logo <<<<<<
try:
    logo_img = PhotoImage(file="typing_logo.png")
    logo_canvas = Canvas(left_frame, width=60, height=60, bg=BG_COLOR, highlightthickness=0)
    logo_canvas.create_image(30, 30, image=logo_img)
    logo_canvas.grid(row=0, column=0, columnspan=2, pady=(0, 10))
except TclError:
    pass

# >>>>>> Title and Description <<<<<<
title_label = Label(left_frame, text="Typing Speed Tester", font=FONT_TITLE, bg=BG_COLOR, fg=FG_COLOR)
title_label.grid(row=1, column=0, columnspan=2, pady=(0, 5))

desc_label = Label(
    left_frame,
    text=f"Type the text below in {TIME_LIMIT} seconds and find out your speed in Words Per Minute (WPM).",
    bg=BG_COLOR, fg=FG_COLOR, justify="center", font=FONT_DESC, wraplength=500
)
desc_label.grid(row=2, column=0, columnspan=2, pady=(0, 20))

# >>>>>> Labels <<<<<<
wpm_label = Label(left_frame, text="WPM", font=FONT_LABEL, bg=BG_COLOR, fg=FG_COLOR)
wpm_label.grid(row=3, column=0, pady=(5, 2))
wpm_box = Label(left_frame, text="--", relief="flat", width=10, height=2, bg=SECONDARY_BG, fg=FG_COLOR, font=FONT_TITLE)
wpm_box.grid(row=4, column=0, padx=10)

time_label = Label(left_frame, text="Time Remaining", font=FONT_LABEL, bg=BG_COLOR, fg=FG_COLOR)
time_label.grid(row=3, column=1, pady=(5, 2))
time_box = Label(left_frame, text="--", relief="flat", width=10, height=2, bg=SECONDARY_BG, fg=FG_COLOR, font=FONT_TITLE)
time_box.grid(row=4, column=1, padx=10)

guidetext_widget = Message(left_frame, text=text_guide, width=500, font=FONT_GUIDE, bg=BG_COLOR, fg=ACCENT_COLOR, justify="left")
guidetext_widget.grid(row=5, column=0, columnspan=2, pady=20)

# >>>>>> Entries <<<<<<
typing_box = Text(left_frame, height=5, width=50, relief="flat", wrap="word", bg=SECONDARY_BG, fg=FG_COLOR,
                  font=FONT_BODY, insertbackground=FG_COLOR, bd=5, selectbackground=ACCENT_COLOR)
typing_box.tag_configure("error", background=ERROR_COLOR, foreground=FG_COLOR)
typing_box.bind("<KeyPress>", start_timer)
typing_box.bind("<KeyRelease>", check_spelling)
typing_box.grid(row=6, column=0, columnspan=2, pady=10)

# >>>>>> Buttons <<<<<<
reset_button = ttk.Button(left_frame, text="Restart", command=reset_game, style="TButton")
reset_button.grid(row=7, column=0, columnspan=2, pady=5)

# >>>>>> Scoreboard <<<<<<
score_title = Label(right_frame, text="Scoreboard", font=FONT_TITLE, bg=SECONDARY_BG, fg=FG_COLOR)
score_title.pack(pady=(10, 0))

score_subtitle = Label(right_frame, text="See where you rank", bg=SECONDARY_BG, fg=FG_COLOR, font=FONT_DESC)
score_subtitle.pack(pady=(0, 10))

scoreboard = ttk.Treeview(right_frame, columns=("Username", "WPM"), show="headings", height=20, style="TTreeview")
scoreboard.heading("Username", text="Username")
scoreboard.heading("WPM", text="WPM")
scoreboard.column("Username", width=120, anchor="center")
scoreboard.column("WPM", width=60, anchor="center")
scoreboard.pack()

load_scores()

