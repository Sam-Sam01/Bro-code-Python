# dictionary = a collection of {key:value} pairs ordered and changeable. No dupes

capitals = {"Usa": "Washington DC", "India": "New Delhi", "China": "Beijing", "Russia": "Moscow"}

print(capitals.get("Usa"))

capitals.update({"Germany": "Berlin"})
print(capitals)
capitals.update({"USA": "Las Vegas"})
print(capitals)
capitals.popitem()
print(capitals)

keys = capitals.keys()
print(keys)

for key in capitals.keys():
    print(key)

values = capitals.values()
print(values)

for value in capitals.values():
    print(value)

items = capitals.items()
print(items)

for key, value in capitals.items():
    print(key, value)