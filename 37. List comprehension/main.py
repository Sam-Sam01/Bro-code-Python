#List comprehension = A concise way to create lists in python Compact and easier to read than 
#                     traditional loops [expression for value in iterable if condition]

doubles = []
""" for x in range(1, 11):
    doubles.append(x*2)

print(doubles) """

# list = [expression for value in iterable if condition]
doubles = [x*2 for x in range(1,11)]
print(doubles)

triples = [y*3 for y in range(1,11)]
print(triples)

squares = [z**2 for z in range(1,11)]
print(squares)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
upper_case_fruits = [fruits.upper() for fruit in fruits]
print(upper_case_fruits)

numbers = [1, -2, 3, -4, 5, -6]
pos_numbers = [num for num in numbers if num >= 0]
neg_numbers = [num for num in numbers if num < 0]
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]
print(pos_numbers)
print(neg_numbers)
print(even_numbers)
print(odd_numbers)

grades = [85, 42, 79, 90, 56, 61, 88, 93, 74, 99, 30]
passing_grades = [grade for grade in grades if grade >= 60]
print(passing_grades)