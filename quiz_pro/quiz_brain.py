class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def nextquestion(self):
        question = self.question_list[self.question_number]
        answer = question.answer
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question.text} (True/False)? ").lower()
        self.check_answer(user_answer, answer)

    def still_have_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_ans, correct_ans):
        if user_ans == correct_ans.lower():
            print('you got it right')
            self.score += 1
        else:
            print("Sorry! wrong answer")

        print(f"correct answer={correct_ans}")
        print(f"your current score is {self.score}/{self.question_number}")
        print("\n\n")
