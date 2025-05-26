class QuizCreator:
    def __init__(self, filename="quiz_questions.txt"):
        self.filename = filename
        
    def create_question(self):
        with open(self.filename, "a") as file:
            while True:
                question = input("\nEnter a question or type 'exit' to exit: ")
                if question.lower() == "exit":
                    break
                
                options = [
                    input("Enter answer a: "),
                    input("Enter answer b: "),
                    input("Enter answer c: "),
                    input("Enter answer d: ")
                ]

                while True:
                    correct_letter = input("\nCorrect answer (a/b/c/d): ").lower()
                    if correct_letter in ['a', 'b', 'c', 'd']:
                        correct_answer = options['abcd'.index(correct_letter)]
                        break
                    print("Invalid input, enter a/b/c/d.")

if __name__ == "__main__":
    creator = QuizCreator()
    creator.create_question()