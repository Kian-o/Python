from data import question_data

"""Quiz Game"""


class Question:

    def __init__(self, text, answer):
        self.text = text
        self.score = 0
        self.answer = answer


question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def quiz_on(self):
        return (self.question_number - 1) < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text}. (True/False)?")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
            self.score -= 1
        print(f"The correct answer was : {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")


quiz = QuizBrain(question_bank)

while quiz.quiz_on():
    quiz.next_question()
