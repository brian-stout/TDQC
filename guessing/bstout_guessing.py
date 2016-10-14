#!usr/bin/env python3

import random

def comparenumberslie(guess, randomNumber):
    if guess == randomNumber:
        return [False, "You guessed right when I was about to lie!"]
    elif guess > randomNumber:
        print(guess, "is too low - please guess again" , end="")
        string = "I lied about " + str(guess) + " being too low"
        return [True, string]
    elif guess < randomNumber:
        print(guess, "is too high - please guess again", end="")
        string = "I lied about " + str(guess) + " being too high"
        return [True, string]

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
    lieOnGuess = random.randint(3,10)
    lieOnGuess = 3 #Hard coded value for debugging purposes
    whenILied = "I didn't lie at all"

    print("Debug:  The random number is:", randomNumber)
    print("Debug:  The program will lie on guess number:", lieOnGuess, "\n\n\n")
    print("I'm thinking of a number from 1 to 100")
    print("Try and guess my number", end="")

    while continueLoop:
        try:
            guess = int(input(": "))
            guessAttempts += 1
            print("Your guess:", guess)
            print("The number of guess currently", guessAttempts)
            print("The program will lie on attempt #:", lieOnGuess)
            if guessAttempts == lieOnGuess:
                continueLoop, whenILied = comparenumberslie(guess, randomNumber)
            else:
                continueLoop = comparenumbers(guess, randomNumber)
        except ValueError:
            print("Illegal value, please type in a number 1-100", end="")
    
    print(guess, "is correct!  You guessed my number in", guessAttempts, "guesses.")
    print(whenILied)

             

if __name__ == "__main__": main()
