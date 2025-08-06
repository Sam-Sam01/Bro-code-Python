# nested loop = A loop within another loop(outer, inner)
# outer loop:
#   inner loop:

for x in range(5):
    for y in range(1, 10):
        print(y,end=" ")
        
    print("\n")

rows = int(input("Enter the num of rows: "))
columns = int(input("Enter the num of columns: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()