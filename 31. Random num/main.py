#random num()

import random

#print(help(random))
# this will show all functions of that method

number = random.randint(1, 6)

print(number)

low = 1
high = 100

number = random.randint(low, high)
print(number)

#random.random() will give number betweem 0 and 1(floating numbers)

number = random.random()
print(number)

options = ("rock", "paper", "scissors")

choice = random.choice(options)
print(choice)

cards = ["jack", "queen", "king", "ace"]
card = random.shuffle(cards)
print(card)