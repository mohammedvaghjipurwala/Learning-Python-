##########################################################
'''
Hangman

Description

Hangman is a popular word guessing game where the player attempts to construct a missing word by guessing one letter at a time. 
After a certain number of incorrect guesses, the game ends and the player loses. The game also ends if the player correctly 
identifies all the letters of the missing word. 

Input

Your program will prompt the user for letter guesses until the word is correctly guessed or the player has exceeded the maximum number of guesses. 
User input should be checked to make sure it's valid. A large file full of words is available for you to use in your program. You will certainly need 
to write some code to filter out the words of a certain length. Perhaps you could prompt the player for the length of the word they would like to guess 
and adjust the number of allowable wrong guesses accordingly. 

Output

Your program should print a list of letters that have been guessed as well as display the correctly guessed letters in the word. 
A graphical representation of the hanging man (kinda gross when you think about it) is optional.

'''
##########################################################
'''
Author : Mohammed Vaghjipurwala (mohammed.vaghjipurwala@gmail.com)
Date : 09/06/2016
'''
##########################################################

#### Import modules/packages

import random
import os

#### Dictionary for pictorial display

hangman = {
    1 : """ ____
|
|
|
""",
2 : """ ____
|   0
|
|
""",
3 : """ ____
|   0
|   |
|
""",
4 : """ ____
|   0
|  /|
|
""",
5 : """ ____
|   0
|  /|\ 
|
""",
6 : """ ____
|   0
|  /|\ 
|  /
""",
7 : """ ____
|   0
|  /|\ 
|  / \ 
"""}

##### Hangman Function/Method

def Hangman(Str,Initial):
    count = 0
    new_str = ''
    while '_' in Initial:
        Input = str(input("Guess a letter : "))
        if Input in new_str:
            print ("You have already guessed this letter. Try again!!!\n")
            continue
        new_str += Input
        new_str += ' '
        print ("Guessed letters: ",new_str)
        if Input in Str:
            Initial_list= list(Initial.replace(" ", ""))
            for i in range(0,len(Str)):
                if Str[i] == Input:
                    Initial_list[i] = Str[i]
            Initial = ' '.join(Initial_list)
            print ("\n",Initial,"\n")
        else:
            count += 1
            print (hangman[count])
            print ("\n",Initial,"\n")
            if count == 7 :
                print ("You're a  Loser.... Go Home...")
                return 25
    
    print ("Yayy!! you Won!!!! I declare you Batman now !!!\n")
    choice = str(input("Do you wanna play again??? (y/n) "))
    os.system('clear')
    if choice == 'y':
        Str = random.choice(words)
        Initial = "_ " * len(Str)
        Hangman(Str,Initial)
    else:
        print ("Well played !!! Bye !!!")
        
##########################################################
########## Script starts here !!!!
##########################################################

if __name__ == "__main__":
    os.system('clear') ### clear screen
    print ("WelCome to HangMan !!!\n     Let's Play \n \n")
    with open("WordsForGames.txt") as word_file:
        words = word_file.read().split()
    Str = random.choice(words) ##### Randomly select a word from the file
    Initial = "_ " * len(Str)
    Hangman(Str,Initial) ####  Function call
