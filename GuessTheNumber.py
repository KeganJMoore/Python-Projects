"""
Kegan Moore
GuessTheNumber.py
Program creates a number in which the user must guess
10/19/2018
"""
import random
number = random.randint(1,10)
while True:
    
    try:
        guess = int(input("Please enter your guess (1-10): "))
        if guess == number:
            break
        else:
            print("Wrong guess. Try again")
    except:
        print("You entered incorrect input")

print("You win")
