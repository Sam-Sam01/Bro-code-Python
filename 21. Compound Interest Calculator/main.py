#Compound interest calculator

principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle amount must be greater than 0")

while rate <= 0:
    rate = float(input("Enter the rate of interest: "))
    if rate <= 0:
        print("Rate of interest must be greater than 0")

while time <= 0:
    time = int(input("Enter the time in years: "))
    if time <= 0:
        print("Time must be greater than 0")

total = principle * ((1 + (rate / 100) ** time))
#total = principle * pow((1 + rate / 100), time)
# same formula

print(f"Balance after {time} year/s: {total:.2f}")