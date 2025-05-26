class quiz_creator:
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
                    
                
                file.write(f"{question}\n")
                for opt in options:
                    file.write(f"{opt}\n")
                file.write(f"{correct_answer}\n")

                print("\nThe inputted question is:", question)
                print("a.", options[0])
                print("b.", options[1])
                print("c.", options[2])
                print("d.", options[3])
                print("The correct answer is:", correct_answer)