# In this file we have written about while loop

# while loop = execute some code WHILE some condition  remains true

name = input("Enter your name: ")

while name == "":
    print("You did not enter your name.")
    name = input("Enter your name: ")

print(f"Hello {name}")

age = int(input("Enter your age: "))

while age < 0:
    print("Age can't be negative.")
    age = int(input("Enter your age: "))

print(f"Your age is {age}")

food = input("Enter a food you like(q to quit): ")

while not food == "q":
    print(f"You like {food}.")
    food = input("Enter a food you like(q to quit): ")

print("Goodbye!")

num = int(input("Enter a number between 1 and 10: "))

while num < 1 or num > 10:
    print("Invalid number.")
    num = int(input("Enter a number between 1 and 10: "))

print(f"You entered {num}.")