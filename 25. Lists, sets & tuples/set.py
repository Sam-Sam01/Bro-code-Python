# Set = {} unordered and immutable, but Add/Remove OK. No Duplicates

fruits ={"apple", "banana", "cherry", "coconut"}

print(fruits)

#indexing does not work in set

fruits.add("pineapple")
print(fruits)

fruits.remove("banana")

#pop()  will take out an element randomly
fruits.pop()