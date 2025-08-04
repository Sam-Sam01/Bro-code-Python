'''Conditional Expressions: A one-line if-else statement.(ternary operator)
Syntax:
variable = expression1 if condition else expression2)
Syntax:
value_if_true if condition else value_if_false'''

num = 5
print("Positive" if num > 0 else "Negative")

num1 = 6
result = "Even" if num1 % 2 == 0 else "Odd"
print(result)

a = 6
b = 7

max_num = a if a> b else b
print(max_num)

min_num = a if a < b else b
print(min_num)

age = 23
status = "Adult" if age >= 18 else "Minor"
print(status)

temp = 30
weather = "Hot" if temp >= 28 else "Cold"
print(weather)

user_role = "admin"
access_level = "Full Access" if user_role == "admin" else "Limited Access"
print(access_level)

