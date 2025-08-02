# calculate the hypotenuse of a right angeled triangle

import math

base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

hypotenuse = math.sqrt(pow(base, 2) + pow(height, 2))

print("The hypotenuse of the triangle is:", round(hypotenuse, 2))