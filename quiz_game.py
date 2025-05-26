import random

class QuizGame:
    def __init__(self, filename="quiz_questions.txt"):
        self.filename = filename
        self.questions = self.load_questions()

    def load_questions(self):
        with open(self.filename, "r") as file:
            lines = file.readlines()
        questions = []
        for line_index in range(0, len(lines), 6):
            if line_index + 5 < len(lines):
                question_text = lines[line_index].strip()
                options = [
                    lines[line_index + 1].strip(),
                    lines[line_index + 2].strip(),
                    lines[line_index + 3].strip(),
                    lines[line_index + 4].strip()
                ]
                correct_answer = lines[line_index + 5].strip()
                questions.append(Question(question_text, options, correct_answer))
        return questions

    def start(self):
        if not self.questions:
            print("No questions available.")
            return

        while True:
            print(f"\n{len(self.questions)} questions are available.")
            try:
                number_of_questions = int(input(f"How many questions would you like to answer? (Max: {len(self.questions)}): "))
            except ValueError:
                print("Invalid input.")
                continue

            number_of_questions = min(number_of_questions, len(self.questions))
            selected_questions = random.sample(self.questions, number_of_questions)
            score = 0

            for question in selected_questions:
                print("\n" + question.text)
                option_labels = ['A', 'B', 'C', 'D']
                for option_index, option_text in enumerate(question.options):
                    print(f"{option_labels[option_index]}) {option_text}")

                while True:
                    user_answer = input("\nEnter the correct answer (a/b/c/d): ").strip().upper()
                    if user_answer in option_labels:
                        break
                    print("Invalid input. Please enter A, B, C, or D.")

                if question.is_correct(option_labels.index(user_answer)):
                    print("Correct!\n")
                    score += 1
                else:
                    print(f"Wrong! The correct answer was: {question.correct_answer}")

            print(f"You got {score} out of {number_of_questions} correct!")
            play_again = input("\nDo you want to restart the quiz? (y/n): ").strip().lower()
            if play_again != 'y':
                print("Thank you for playing!")
                break
