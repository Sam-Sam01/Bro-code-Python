#function = a block of reusable code
#           place () after the function name to invoke it

def happy_birthday(name, age):
    print(f"happy birthday to {name}!")
    print(f"You are {age} years old!")
    print("happy birthday to you!")
    print()

happy_birthday("Sany", 25)

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount} is due on {due_date}.")

display_invoice("Sany", 100, "12/25/2023")