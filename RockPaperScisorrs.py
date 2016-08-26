##################################################
#
#Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), 
#compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
#
##################################################
import sys

print("\033c") ### clear screen 
user1 = input("What's your name? ")
print("\033c")
user2 = input("And your name? ")

def compare(u1, u2):
    if u1 == u2:
        return("It's a tie!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return(user1 + " wins!")
        else:
            return(user2 + " wins!")
    elif u1 == 'scissors':
        if u2 == 'paper':
            return(user1 + " wins!")
        else:
            return(user2 + " wins!")
    elif u1 == 'paper':
        if u2 == 'rock':
            return(user1 + " wins!")
        else:
            return(user2 + " wins!")
    else:
        return("Invalid input! You have not entered rock, paper or scissors, try again.")
        sys.exit()
while True:
    print("\033c")
    user1_answer = input("%s, do yo want to choose rock, paper or scissors?" % user1)
    print("\033c")
    user2_answer = input("%s, do you want to choose rock, paper or scissors?" % user2)
    print(compare(user1_answer, user2_answer))
    Quit = input("To exit press q  &  to continue press any character :: ")
    if Quit == "q":
        print ("Well Played !!! Bye.")
        break
