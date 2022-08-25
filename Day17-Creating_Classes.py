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
        print(f"The correct answer was : {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")


quiz = QuizBrain(question_bank)

while quiz.quiz_on():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

"""Notes"""


class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "michael")
User_2 = User("001", "angela")

# user_1 = User()
# user_1.id = "001"
# user_1.username = "michael"
#
# print(user_1.username)

"""Constructor: part of the blueprint that allows us to specify what should happen when object is constructed.
Also known as initializing an object: to set variables, counters etc. to their starting values at the beginning
of a program or subprogram."""

"""init function:"""


class Car:
    def __init__(self, seats):
        self.seats = seats
        # initialise attributes

    def enter_race_mode(self):
        self.seats = 2


"""PascalCase: The first letter of each word is capitalized"""
"""camelCase: The first word is lower cased and each subsequent word is capitalized """
"""snake_case: all words are lower case and separated by underscore"""

"""Methods are the thing that the object does. See enter_race_mode in Car class"""
