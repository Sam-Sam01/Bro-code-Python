# for loop = execute a block of code a fixed number of times.
#            You can iterate over a range, string, sequence, etc.

for x in range(1, 11):
    print(x)

print("\n")
print("Happy New year!")
print("\n")

for x in reversed(range(1, 11)):
    print(x)

print("\n")

credit_card = "1234-5678-9012-3456"

for x in credit_card:
    print(x)

print("\n")

for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)

print("\n")

for x in range(1, 21):
    if x == 13:
        break
    else:
        print(x)