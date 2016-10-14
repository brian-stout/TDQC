#!usr/bin/env python3

import random

def comparenumbers(guess, randomNumber):
    """This function compares two values, determines if it is equivalent,
       greater than, or less than.  It then prints a string letting the
       player know which it is.
       
       It returns a bool value of False if the values are equivalent which
       tells the program to stop running the loop because the player won
       """

    if guess == randomNumber:
        return False
    elif guess > randomNumber:
        print(guess, "is too high - please guess again", end="")
        return True
    else:
        print(guess, "is too low  - please guess again", end="")
        return True

def comparenumberslie(guess, randomNumber):
    """This function does the same thing as comparenumbers() but lies about the results

       Additionally it returns a string stating which number it lied about so it
       can be called later.  This function return both objects in a list instead
       of a tuple to cut back on code lines and to make it clearer to read.
       The reason is because a tuple can't unpack directly from a function return
       """

    if guess == randomNumber:
        return [False, "You guessed right when I was about to lie!"]
    elif guess > randomNumber:
        print(guess, "is too low  - please guess again" , end="")
        string = "I lied about " + str(guess) + " being too low"
        return [True, string]
    else:
        print(guess, "is too high - please guess again", end="")
        string = "I lied about " + str(guess) + " being too high"
        return [True, string]

def shouldlie(percent):
    """A function that returns true or false based on a hard coded percentage.  
       The function determines if it is a float or an INT, to solve for
       the possible ways percentages might be wrote
       EX: 0.3 will have a 30% chance of returning true
       EX: 30 will have a 30% chance of returning true
       """
    if type(percent) == float:
        return percent > random.random()
    elif type(percent) == int:
        return percent > random.randint(1,100)

def main():

    randomNumber = random.randint(1,100)
    guessAttempts = 0
    continueLoop = True
    haveLied = False

    whenILied = "I didn't lie at all"
    invalidInput = "is an invalid input, please type in a number 1-100"

    print("I'm thinking of a number from 1 to 100")
    print("Try and guess my number", end="")

    while continueLoop:
        try:
            guess = input(": ")

            #Gives a valid way for user to exit program
            if guess == "end":
                exit()
            #Checks for empty value
            if guess == "":
                guess = "Not entering a value"  #Corrects returned error
                raise ValueError
            #Raises an error if value has a leading 0 or decimal
            if guess != str(int(guess)):
                raise ValueError
            #Checks for value outside of range
            guess = int(guess)
            if (guess < 1) or (guess > 100):
                raise ValueError

            guessAttempts += 1
            #Determines if program should lie based on percent
            if (shouldlie(.25) and haveLied == False):
                continueLoop, whenILied = comparenumberslie(guess, randomNumber)
                haveLied = True
            else:
                #Assigns continueLoop False if player wins
                continueLoop = comparenumbers(guess, randomNumber)

        #Handles all the exceptions in the program
        except ValueError:
            print(guess, invalidInput, end="")
 
    print(guess, "is correct!  You guessed my number in", guessAttempts, "guesses.")
    print(whenILied)

             
if __name__ == "__main__": main()
