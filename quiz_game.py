class quiz_game:
    def __init__(self, filename="quiz_questions.txt"):
        self.filename = filename
        self.questions = self.load_questions()