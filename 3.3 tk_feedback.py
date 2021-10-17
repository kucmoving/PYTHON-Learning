def true_pressed():
    self.give_feedback(quiz.check_answer("True"))

def false_pressed():
    self.give_feedback(quiz.check_answer("False"))
    self.give_feedback(is_right)


def give_feedback(is_right):
    if is_right:
        canvas.config(bg="green")
    else:
        canvas.config(bg="red")
    window.after(1000, get_next_question)

def get_next_question(self):
    self.canvas.config(bg="white")
    if self.quiz.still_has_questions():
        self.score_label.config(text=f"Score: {self.quiz.score}")
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
    else:
        self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
