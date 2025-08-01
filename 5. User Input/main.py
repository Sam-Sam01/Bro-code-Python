'''input() = A funcption that prompts the user to enter data
            Returns the entered data as a string'''

name =input("What is your name?")
age = input("How old are you?")

print(f"Hello {name}! You are {age} years old.")
# input takes only string so we need to typecast for other data types

age = int(age)
age = age+1
print(f"Next year you will be {age} years old.")