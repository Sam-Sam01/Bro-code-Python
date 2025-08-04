#logical operators = evaluate multiple conditions in same line
''' OR = at least one condition must be true
    AND = all conditions must be true
    NOT = reverses the condition
'''

temp = int(input("Enter the temp: "))
is_sunny = True
is_cold = True
is_raining = False

if temp > 10 and not is_raining:
    print("We will enjoy rain from home and drink hot cocoa.")
elif temp < 10 and is_cold:
    print("We will stay at home.")
elif temp > 20 or is_sunny:
    print("We will go out.")