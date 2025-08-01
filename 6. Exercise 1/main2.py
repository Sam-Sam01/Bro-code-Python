# Exercise 2 Shopping cart program

item = input("What item would you like to buy? ")
price = float(input("What is the price of the item? "))
quantity = int(input("How many would you like? "))

total = price * quantity

print(f"You have bought {quantity} X {item}(s)")
# round() function returns a floting number with the specified number of decimals.
print(f"Your total is: ${round(total, 2)}")