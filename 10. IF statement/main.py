# if = Do some code only IF some condition is true

age = int(input("Enter your age: "))

if age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You must be 18+ to sign up.")

response = input("Would you like food? (Y/N): ")

if response == "Y":
    print("Here is your food.")
elif response == "N":
    print("Fine, thanks.")
else:
    print("Invalid response.")

print("Have a nice day!")

online = True

if online:
    print("You are now connected.")
else:
    print("You are now disconnected.")

print("Have a nice day!")