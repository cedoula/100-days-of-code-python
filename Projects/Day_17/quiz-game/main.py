from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

#Create a list of question objects
question_bank = [Question(question["question"], question["correct_answer"]) for question in question_data]

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz.\nYour final score was: {quiz.score}/{quiz.question_number}.")