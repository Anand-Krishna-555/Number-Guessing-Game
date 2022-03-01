# importing required modules
import math
import random

# Getting the upper and lower bound from "user"
upper = int(input("Enter the upper bound: "))
lower = int(input("Enter the lower bound: "))

x = random.randint(lower, upper)

# Calculating the minimum number of guesses
y = round(math.log(upper - lower + 1, 2))
print("You have", y, "chances to guess")

# Container for carry the value
count = 0
while count < y:
    count += 1

    guess = int(input("Enter the number: "))
    if x == guess:
        print("You've guessed the correct number")
        break
    elif x < guess:
        print("You've guessed too high")
    else :
        print("You've guessed too small")

if count > y:
    print("Better luck next time")