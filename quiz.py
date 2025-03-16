# Multiple Choice Quiz

def run_quiz():
    questions = [
        {
            "question": "What is the capital of France?",
            "choices": ["A) Paris", "B) London", "C) Berlin", "D) Madrid"],
            "answer": "A"
        },
        {
            "question": "Which programming language is known as the language of the web?",
            "choices": ["A) Python", "B) JavaScript", "C) Java", "D) C++"],
            "answer": "B"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "choices": ["A) Earth", "B) Jupiter", "C) Mars", "D) Saturn"],
            "answer": "B"
        },
        {
            "question": "Who directed the movie 'Inception'?",
            "choices": ["A) Christopher Nolan", "B) Steven Spielberg", "C) Quentin Tarantino", "D) Martin Scorsese"],
            "answer": "A"
        },
        {
            "question": "What is the output of 2 + 2?",
            "choices": ["A) 3", "B) 4", "C) 5", "D) 6"],
            "answer": "B"
        }
    ]

    score = 0

    for q in questions:
        print(q["question"])
        for choice in q["choices"]:
            print(choice)
        answer = input("Your answer: ").strip().upper()
        if answer == q["answer"]:
            score += 1
            print("Correct!\n")
        else:
            print(f"Wrong! The correct answer was {q['answer']}.\n")

    print(f"Your final score is {score}/{len(questions)}.")
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        run_quiz()

if __name__ == "__main__":
    run_quiz()
