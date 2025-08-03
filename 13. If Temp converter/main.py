# temp converter

temp = float(input("Enter the temp: "))

unit = input("F/C/K: ")

if unit.upper() == "F":
    print(f"In Celsius: {(temp - 32) * 5/9} & In Kelvin: {(temp - 32) * 5/9 + 273.15}")
elif unit.upper() == "C":
    print(f"In Fahrenheit: {temp * 9/5 + 32} & In Kelvin: {temp + 273.15}")
elif unit.upper() == "K":
    print(f"In Celsius: {temp - 273.15} & In Fahrenheit: {(temp - 273.15) * 9/5 + 32}")
else:
    print("Invalid input")