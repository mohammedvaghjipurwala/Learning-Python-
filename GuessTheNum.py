################# http://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html

import random

def start_game():
	num = int(input("Guess the number between 1 and 9 --> "))
	game(num)	

def game(num):
	attempt = 1 
	keep = True
	randnum = random_number()
	while num > 0:

		if num > randnum:
			print("**Too high!!, keep trying or type exit to exit the Game**")
			attempt = attempt + 1
			num = keep_trying()			

		if num < randnum:
			print("**Too low!!, keep trying or type exit to exit the Game**")
			attempt = attempt + 1
			num = keep_trying()
		
		if num == randnum:
			print("**You won!, %d was the number**" %randnum)
			print("Number of attempts %d" %attempt)
			num = -1	
			
			
def keep_trying():

	new_num = str(input("1-9 or exit --> "))
	if new_num == 'exit':
		new_num = -1
		return (new_num)
	else:
		return int(new_num)
	
def random_number():
	randnum = random.randint(1,9)
	return randnum
			 
start_game()
