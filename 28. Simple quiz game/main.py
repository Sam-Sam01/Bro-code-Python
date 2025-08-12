#python quiz game

questions = ("How many elements are in the periodic table?", "Which animal lays  the largest eggs?", "What is the most abundant gas in Earth's atmosphere?", "How many hearts does an Octopus have?", "How many bones does an adult human have?",)

options = (("A. 118", "B. 119", "C. 120", "D. 121"), ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"), ("A. Nitrogen", "B. Oxygen", "C. Carbon Dioxide", "D. Hydrogen"), ("A. 3", "B. 4", "C. 5", "D. 6"), ("A. 206", "B. 207", "C. 208", "D. 209"),)

answers = ("A","D","A","A","A")
guesses = []
score = 0
questionNum = 0

for question in questions:
    print("------------------")
    print(question)
    for option in options[questionNum]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[questionNum]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[questionNum]} is the correct answer")
    questionNum += 1

print("------------------")
print("       RESULTS    ")
print("------------------")

print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")