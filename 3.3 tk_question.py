#4. 套取字典成想要的形式
question_bank = []
for question in question_data:##question_data是一個字典，引入組合用
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
quiz = QuizBrain(question_bank)

#剩餘問題
def still_has_questions():
    return question_number < len(question_list)

##下一條問題
def next_question(self):
    current_question = question_list[question_number]
    question_number += 1
    user_answer = input(f"Q.{question_number}: {current_question.text} (True/False): ")
    self.check_answer(user_answer)

##檢查答案
def check_answer(user_answer):
    correct_answer = current_question.answer
    if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
            return True
        else:
            print("That's wrong.")
            return False

        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")





##########OBJECT
class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {self.current_question.text} (True/False): ")
        self.check_answer(user_answer)

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
            return True
        else:
            print("That's wrong.")
            return False

        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")