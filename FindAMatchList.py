#######################################################################################
#Take two lists, say for example these two:

#  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

#Extras:
#1.Randomly generate two lists to test this
#2.Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
###################################################################################################

import random

print ("Generating 2 random lists, please wait...")
a = [random.randrange(1,101) for i in range(random.randrange(3,20))]
b = [random.randrange(1,101) for i in range(random.randrange(3,20))]

print(list(set([y for x in a for y in b if x == y ])))
