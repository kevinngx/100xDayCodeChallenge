# TODO: asking the question
# TODO: checking if the answer is right
# TODO: checking if we're at the end of the quiz

class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def check_answer(self, question, user_answer):
        print(f"The correct answer was: {question.answer}")
        if question.answer.lower() == user_answer:
            self.score += 1
            print("You got it right!")
            return True
        print("You got it wrong :(")
        return False

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}. {current_question.text} (True/False): ").lower()
        self.check_answer(current_question, user_answer)
        print(f"Your current score is: {self.score}/{self.question_number}")

    def still_has_questions(self):
        if self.question_number == len(question_list):
            return True
        return False