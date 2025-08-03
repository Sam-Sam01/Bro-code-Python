# this is a basic calculator only using if statement

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

op = input("Enter an operator (+, -, *, /): ")

if op == "+" :
    print(f"The sum of {num1} and {num2} is {num1 + num2}.")
elif op == "-" :
    print(f"The difference of {num1} and {num2} is {num1 - num2}.")
elif op == "*" :
    print(f"The product of {num1} and {num2} is {num1 * num2}.")
elif op == "/" :
    print(f"The quotient of {num1} and {num2} is {round(num1 / num2, 2)}.")
else:
    print("Invalid operator.")

print("Have a nice day!")