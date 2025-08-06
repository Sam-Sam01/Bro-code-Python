#another way to write the compound interest calculator

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Priciple have to be greater than 0")
    else:
        break

while True:
    rate = float(input("Enter the rate of interest: "))
    if rate < 0:
        print("Rate have to be greater than 0")
    else:
        break
    
while True:
    time = int(input("Enter the time in years: "))
    if time < 0:
        print("Time have to be greater than 0")
    else:
        break

total = principle * pow((1+ rate/100), time)
print(f"Balance after {time} year/s: {total:.2f}")