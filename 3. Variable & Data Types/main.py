# Variable = A container for a value(string, integer,...)

#Strings
first_name = 'Shamiul'
last_name = 'Haque'

print(first_name)

#F-string allows you to format selected parts of a string.
full_name = f'{first_name} {last_name}'
print(f"Hello, {full_name}.")
food = 'Burger'
print(f"You like {food}?")

#Integers
#don't put '' then it not will be integer, it will become string
age = 25
print(f"You are {age} years old.")

#float
price = 10.33
print(f"The coffe price is ${price}.")

#boolean
#true or false
is_student = True
print(f"Are you a student  {full_name}? {is_student}")


