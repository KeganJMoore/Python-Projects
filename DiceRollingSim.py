"""
Simulates rolling a pair of dice
"""

import random

while True:
    numDice = input("Would you like to roll the dice?")
    if numDice in ("yes", "y", "Yes", "Y"):
        Dice = random.randint(1, 6)
        print(Dice)
    elif numDice in ("no", "n", "No", "N"):
        break
    else:
        print("I'm sorry, that imput is invalid. Try again.")
