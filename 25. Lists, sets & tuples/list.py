# collection = single "variable"used to store multiple values
# List = [] ordered and changable. Duplicates OK
# Set = {} unordered and immutable, but Add/Remove OK. No Duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. Faster

fruits = ["apple", "banana", "cherry"]
print(fruits[::-1])
for fruit in fruits:
    print(fruit)

""" fruits[3] = "pineapple"
for fruit in fruits:
    print(fruit) 
This is not the way it will work."""

fruits.append("pineapple")
for fruit in fruits:
    print(fruit)

fruits.remove("banana")
for fruit in fruits:
    print(fruit)

fruits.insert(0, "orange")
for fruit in fruits:
    print(fruit)

fruits.sort()
for fruit in fruits:
    print(fruit)

fruits.reverse()
for fruit in fruits:
    print(fruit)

#fruits.clear() this will clear the list

print(fruits.index("apple"))

print(fruits.count("banana"))
print(fruits)
fruits.clear()
print(fruits)