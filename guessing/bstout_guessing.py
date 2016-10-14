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
    elif guess < randomNumber:
        print(guess, "is too low - please guess again", end="")
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
        print(guess, "is too low - please guess again" , end="")
        string = "I lied about " + str(guess) + " being too low"
        return [True, string]
    elif guess < randomNumber:
        print(guess, "is too high - please guess again", end="")
        string = "I lied about " + str(guess) + " being too high"
        return [True, string]

def main():

#TODO: Remove lieOnGuess debug value
#TODO: Remove the debug print statements
#TODO: Create a weighted random choice between True and False for the random lie attempt
#TODO: Change the guess INT conversion to handle strings exclusively so that Python can
#      determine when exceptions should happen
#TODO: PEP-8 Compliance
#TODO: Comment more stuff
#TODO: Raise an error when user inputs number not between 0-101

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
            guess = input(": ")

            #Gives a valid way for user to exit program
            if guess == "end":
                exit()
            guess = int(guess)

            #Raises an error if the value is not from 1 to 100
            if (guess < 1) or (guess > 100):
                raise ValueError
            guessAttempts += 1

            #Debug lines
            print("Your guess:", guess)
            print("Debug: The number of guess currently", guessAttempts)
            print("Debug: The program will lie on attempt #:", lieOnGuess)

            #Determines if the program should lie on this guess attempt
            #Runs normally if it's not a lie, returns bool value to continue loop
            #To determine if user has won and the loop should stop.
            if guessAttempts == lieOnGuess:
                continueLoop, whenILied = comparenumberslie(guess, randomNumber)
            else:
                continueLoop = comparenumbers(guess, randomNumber)

        except ValueError:
            print("Illegal value, please type in a number 1-100", end="")
        except EOFError:
            print(" Type end to terminate the program correctly")
        except KeyboardInterrupt:
            print(" Type end to terminate the program correctly")
        except TypeError:
            print("Illegal characters, please type in a number 1-100", end="")
    
    print(guess, "is correct!  You guessed my number in", guessAttempts, "guesses.")
    print(whenILied)

             
if __name__ == "__main__": main()
