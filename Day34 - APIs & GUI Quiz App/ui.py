from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self,quiz_brain: QuizBrain):
        self.score = 0
        self.question_number = 0
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        # CANVAS
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150,125,
                                                 width= 280,
                                                 text="Quiz Fact Here",
                                                 font=("Arial", 15, "italic"))
        self.canvas.grid(row=1,column=0, columnspan=2)

        # BUTTONS
        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_bt_clicked)
        self.false_button.grid(row= 2, column= 0, pady= 50)
        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0,command=self.true_bt_clicked)
        self.true_button.grid(row= 2, column= 1, pady=50)

        # LABELS
        self.score_label = Label(text=f"Score:{self.score}/{self.question_number}", bg=THEME_COLOR, fg="white",
                                 font=("Arial", 12, "bold"), pady=50)
        self.score_label.grid(row= 0, column= 1)

        self.get_next_question()


        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text= f"You completed the quiz!\n"
                                                             f"  Final Score is {self.score}/{self.question_number}")
            self.true_button.config(state= "disabled")
            self.false_button.config(state="disabled")

    def true_bt_clicked(self):
        is_right = self.quiz.check_answer(user_answer="True")
        self.give_feedback(is_right)

    def false_bt_clicked(self):
        is_right = self.quiz.check_answer(user_answer="False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.score += 1
            self.question_number += 1
            self.score_label.config(text=f"Score: {self.score}/{self.question_number}")
        else:
            self.canvas.config(bg="red")
            self.question_number += 1
            self.score_label.config(text=f"Score: {self.score}/{self.question_number}")
        self.window.after(1000, self.get_next_question)
