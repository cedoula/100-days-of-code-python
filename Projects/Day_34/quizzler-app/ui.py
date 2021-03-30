from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain):
        self.quiz = quiz_brain

        self.window = Tk() 
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.score_label = Label()
        self.score_label.config(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)
        
        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.question = self.canvas.create_text(
            150, 
            125,
            width=280, 
            text="Hello", 
            fill=THEME_COLOR, 
            font=("Arial", 20, "italic")
        )
        
        TRUE_IMG = PhotoImage(file="images/true.png")
        FALSE_IMG = PhotoImage(file="images/false.png")
        self.true_button = Button(image=TRUE_IMG, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column=0, row=2)
        self.false_button = Button(image=FALSE_IMG, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="'You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(ms=1000, func=self.get_next_question)
        