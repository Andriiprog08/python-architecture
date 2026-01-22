import random

numbers = random.randint(0,10)
your_number = float(input("Write a number from 0 to 10: "))

if your_number == numbers:
    print("You guessed the number")
else:
    print("You didn't guess, try again")

while your_number != numbers:
    your_number = float(input("You have a second chance: "))
    if your_number == numbers:
        print("You guessed the number")
    else:
        print("You lost, game over, the computer had a number: " + str(numbers))
    break