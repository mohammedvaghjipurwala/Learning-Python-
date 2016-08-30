######################################################################
'''
You, the user, will have in your head a number between 0 and 100. The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.

At the end of this exchange, your program should print out how many guesses it took to get your number.

As the writer of this program, you will have to choose how your program will strategically guess. A naive strategy can be to simply start the guessing at 1, and keep going (2, 3, 4, etc.) until you hit the number. But that’s not an optimal guessing strategy. An alternate strategy might be to guess 50 (right in the middle of the range), and then increase / decrease by 1 as needed. After you’ve written the program, try to find the optimal strategy! (We’ll talk about what is the optimal one next week with the solution.)

'''
######################################################################

import random
up = 100
low = 0
attempt = 0
def GuessTheNumber(low,up,attempt):
    
    Guess = random.randint(low,up)
    print ("The computer guessed :: ",Guess)
    Input = str(input("type h for 'high' l for low or e for equal : "))
    
    if Input == 'e' :
        attempt += 1
        print ("Yayy !!!  you have guessed the correct number in ",attempt," attempts ....")
    elif Input == 'h' :
        print ("You have guessed High \n Try again!!!")
        attempt += 1
        GuessTheNumber(low,Guess,attempt)
    elif Input == 'l' :
        print ("You have guessed low \n Try again!!!")
        attempt += 1
        GuessTheNumber(Guess,up,attempt)
        
if __name__ == "__main__":
    input("Think of a number between 0 - 100 ")
    GuessTheNumber(low,up,attempt)
