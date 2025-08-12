# Guess the number with random()

import random

lowest_num = 1
highest_num = 123

answer = random.randint(lowest_num, highest_num)

guesses = 0
is_running = True

print("Python Number Guess")
print(f"Guess a number between {lowest_num} and {highest_num}.")
while is_running:
    user_num = int(input("Guess the number(1-123): "))
    if user_num == answer:
        is_running = False
    elif user_num > answer:
        print("Too High.")
        guesses+= 1
    else:
        print("Too low.")
        guesses+= 1

print(f"You geussed it in {guesses} guesses.")
print("Thanks for playing.")
print("The answer was", answer)
print("Bye!")