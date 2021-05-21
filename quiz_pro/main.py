from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
Question_bank = []
for i in question_data:
    Question_bank.append(Question(i['question'], i['correct_answer']))

quiz = QuizBrain(Question_bank)

while quiz.still_have_question():
    quiz.nextquestion()
print("\n\n\n\n")
print("Congrats you have completed the quiz")
print(f"your final score is {quiz.score}/{quiz.question_number}")