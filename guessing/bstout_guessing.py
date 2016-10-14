#!usr/bin/env python3

import random

def main():

    randomNumber = random.randint(1,100)
    guessAttempts = 0

    print("Debug:  The random number is:", randomNumber, "\n\n\n")
    print("I'm thinking of a number from 1 to 100")
    guess = int(input("Try and guess my number: "))
    while True:
        if guess == randomNumber:
            print(guess, "is correct! You guessed my number in", guessAttempts)
            break
        elif guess > randomNumber:
            print(guess, "is too high - please guess again", end="")
            guessAttempts += 1
        elif guess < randomNumber:
            print(guess, "is too low - please guess again", end="")
            guessAttempts += 1
        guess = int(input(": "))
        
        

if __name__ == "__main__": main()
