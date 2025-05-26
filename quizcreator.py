class QuizCreator:
    def __init__(self, filename="quiz_questions.txt"):
        self.filename = filename
        
    def create_question(self):
        with open(self.filename, "a") as file:
            while True:
                question = input("\nEnter a question or type 'exit' to exit: ")
                if question.lower() == "exit":
                    break