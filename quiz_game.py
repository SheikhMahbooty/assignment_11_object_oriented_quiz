class quiz_game:
    def __init__(self, filename="quiz_questions.txt"):
        self.filename = filename
        self.questions = self.load_questions()
        
    def load_questions(self):
        with open(self.filename, "r") as file:
            lines = file.readlines()
        questions = []
        for i in range(0, len(lines), 6):
            if i + 5 < len(lines):
                q_text = lines[i].strip()
                opts = [lines[i+1].strip(), lines[i+2].strip(), lines[i+3].strip(), lines[i+4].strip()]
                correct = lines[i+5].strip()
                questions.append(Question(q_text, opts, correct))
        return questions
