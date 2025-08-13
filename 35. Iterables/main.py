#Iterables = An object/collection that can return its elements one at a time, allowing it to 
#            be iterated over a loop

numbers = [1,2,3,4,5]
nums = (1,2,3,4,5)
fruits = {'apple', 'orange', 'banana', 'coconut'} #sets cannont ne reversable
name = "Sany"
my_dictionary = {"A": 1, "B": 2, "C": 3}

for number in  numbers:
    print(number)

for value in my_dictionary.values():
    print(value)

for key, value in my_dictionary.items():
    print(f"{key} = {value}")