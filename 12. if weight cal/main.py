# weight converter

weight = float(input("Enter your weight is: "))
base_weight = weight
unit = input("(L)bs or (K)g: ")

if  unit.upper() == "L":
    weight = weight * 0.45
    print(f"You are {weight} kilos and in {base_weight} pounds")    
elif unit.upper() == "K":
    weight = weight / 0.45
    print(f"You are {weight} pounds and in {base_weight} kilos")
else:
    print("Invalid input")