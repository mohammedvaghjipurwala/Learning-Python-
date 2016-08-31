####################################################################################################
'''
Create a tic tac toe game
'''
####################################################################################################

Start_Mat = [[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]]

def DrawBoard(rows,cols,game):
    dash = " ---"
    pipe = "|"
    k = 1
    for cnt in range(0,rows):
        if cnt % 2 == 0:
            print (dash * (cols))
        else:
            for j in range(0,cols):
                if j != cols - 1:
                    print (pipe,game[cnt - k][j],"",end="", flush=True) 
                else:
                    print (pipe,game[cnt - k][j] ,"|")
            k +=1
    return 0
            

def CheckGame(grid):
	# rows
	for x in range(0,3):
		row = set([game[x][0],game[x][1],game[x][2]])
		if len(row) == 1 and game[x][0] != 0:
		    return game[x][0]

	# columns
	for x in range(0,3):
		column = set([game[0][x],game[1][x],game[2][x]])
		if len(column) == 1 and game[0][x] != 0:
		    return game[0][x]

	# diagonals
	diag1 = set([game[0][0],game[1][1],game[2][2]])
	diag2 = set([game[0][2],game[1][1],game[2][0]])
	if len(diag1) == 1 or len(diag2) == 1 and game[1][1] != 0:
	    return game[1][1]

	return 1
	
def TicTacToeInput(game,i):
    if any(0 in s for s in game):
        if i % 2 != 0:
            Player = "X"
        else:
            Player = "O"
            
        DrawBoard(7,3,game)
        
        print ("\nPlayer ",Player," Turn!!! \n")
        row = int(input("Enter the row (1-3): ")) - 1
        col = int(input("Enter the column (1-3): ")) - 1
        
        if game[row][col] == 0:
            game[row][col] = Player
            i += 1
            
            if i >= 5:
                Check = CheckGame(game)
                if Check != 1:
                   print("Congratulations", Check, ",You Won!!!")
                   if input("Do you want to play again (y/n): ") == 'n':
                       print ("Thanks for playing!!! Bye!!!")
                       return 0
                   else:
                       TicTacToeInput(Start_Mat,1)
            
            TicTacToeInput(game,i)
        else:
            print ("Invalid position please Try again")
            DrawBoard(7,3,game)
            TicTacToeInput(game,i)
    
    if CheckGame(game) == 1:
        print ("Its a Draw !!!!")

if __name__ == "__main__":
    print ("Welcome to Tic Tac Toe !!!")
    print ("\n Let's Play !!!!\n")
    TicTacToeInput(Start_Mat,1)
