#Membership operators = used to test whether a value or variable is found in a sequence
#                       (string, list, tuple, set or dictionary)
#                       1. in
#                       2. not in


word = "Apple"

letter = input("Guess a letter in the secret word: ")

if letter in word:
    print(f"There is a {letter}.")
else:
    print(f"{letter} was not found.")

students = {"sany", "Sam", "Reza"}
student = input("Enter the name of a student: ")

if student in students:
    print(f"{student} is a student.")
else:
    print(f"{student} is not a student.")

grades = {"Sandy": "A", "Sam": "B", "Sany": "C", "Reza": "D"}
student = input("Enter the name of a student: ")

if student in grades:
    print(f"{student} has a grade of {grades[student]}.")
else:
    print(f"{student} has not been found.")

email = "sam@gmail.com"

if "@" in email and "." in email:
    print("Valid email.")
else:
    print("Ivalid email.")