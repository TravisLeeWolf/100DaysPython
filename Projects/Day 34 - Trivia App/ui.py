from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")
TICK_FILENAME = ".\images\\true.png"
CROSS_FILENAME = ".\images\\false.png"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain): #quiz_brain: QuizBrain NOTE: Specifying the file type needed to be added 
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler [Tech Edition]")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score label
        self.score_label = Label(text="Score: ", font=FONT, fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        # Quiz block
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Question Text", fill=THEME_COLOR, font=FONT)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # True button
        tick_image = PhotoImage(file=TICK_FILENAME)
        self.true_button = Button(image=tick_image, bg=THEME_COLOR, highlightthickness=0, relief=FLAT, command=self.true_pressed)
        self.true_button.grid(column=0, row=2)

        # False button
        cross_image = PhotoImage(file=CROSS_FILENAME)
        self.false_button = Button(image=cross_image, bg=THEME_COLOR, highlightthickness=0, relief=FLAT, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            quiz_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=quiz_text, fill=THEME_COLOR)
        else:
            self.canvas.config(bg=THEME_COLOR)
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.\nThank you for playing!", fill="white")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer(user_answer="True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer(user_answer="False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.canvas.itemconfig(self.question_text, fill="white")
        else:
            self.canvas.config(bg="red")
            self.canvas.itemconfig(self.question_text, fill="white")
        self.window.after(1000, self.get_next_question)