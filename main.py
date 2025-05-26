if __name__ == "__main__":
    print("1. Create quiz questions")
    print("2. Take the quiz")
    choice = input("Choose an option (1/2): ")

    if choice == "1":
        creator = QuizCreator()
        creator.create_question()
    elif choice == "2":
        quiz = QuizGame()
        quiz.start()
    else:
        print("Invalid choice.")