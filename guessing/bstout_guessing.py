#!usr/bin/env python3

import random

def comparenumbers(guess, randomNumber):
    if guess == randomNumber:
        return False
    elif guess > randomNumber:
        print(guess, "is too high - please guess again", end="")
        return True
    elif guess < randomNumber:
        print(guess, "is too low - please guess again", end="")
        return True

def main():

    randomNumber = random.randint(1,100)
    guessAttempts = 0
    continueLoop = True

    print("Debug:  The random number is:", randomNumber, "\n\n\n")
    print("I'm thinking of a number from 1 to 100")
    print("Try and guess my number", end="")

    while continueLoop:
        try:
            guess = int(input(": "))
            continueLoop = comparenumbers(guess, randomNumber)
            guessAttempts += 1
        except ValueError:
            print("Illegal value, please type in a number 1-100", end="")
    
    print(guess, "is correct!  You guessed my number in", guessAttempts)

             

if __name__ == "__main__": main()
