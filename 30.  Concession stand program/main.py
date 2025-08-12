# consession stand program

menu = {"pizza": 10.50, "burger": 8.50, "fries": 4.50, "salad": 6.50, "soda": 2.50, "water": 1.50, "pop-corn": 6.00}


cart = []
total = 0

print("------------------MENU------------------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("----------------------------------------")

while True:
    food = input("What would you like to order? (type 'done' to finish): ")
    if food.lower == "done":
            break
    elif menu.get(food) is not None:
        cart.append(food)
        #total += menu[food]

print("----------------Your Order----------------")
for food in cart:
    total += menu.get(food)
    print(food, end= " ")

print()
print(f"Total is ${total:.2f}")