class Question_List:
    def __init__(self, text, options, correct_answer):
        self.text = text
        self.options = options
        self.correct_answer = correct_answer
        
    def is_correct(self, answer_index):
        return self.options[answer_index] == self.correct_answer