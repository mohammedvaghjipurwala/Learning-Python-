#######################################################################
'''
Time for some fake graphics! Let’s say we want to draw game boards that look like this:

 --- --- --- 
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- --- 

This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes (8x8 for chess, 19x19 for Go, and many more).

Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.

'''
#######################################################################

def DrawBoard(rows,cols):
    dash = " ---"
    pipe = "|   "
    for i in range(0,rows):
        if i % 2 == 0:
            print (dash * (cols))
        else:
            print (pipe * (cols + 1))
            
def UserInput():
    print ("Enter the size of the board:: \n")
    rows = (int(input("Enter the number of rows: ")) * 2) + 1
    cols = int(input("Enter the number of cols: "))
    return (rows,cols)
    
if __name__ == "__main__":
    row, col = UserInput()
    DrawBoard(row, col)
