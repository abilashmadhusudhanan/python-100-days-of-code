from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []

for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()
    print(f"You current score is {quiz_brain.score} / {quiz_brain.question_number}")
    print("\n")

print("You have completed the quiz")
print(f"Your total score is {quiz_brain.score} / {quiz_brain.question_number}")