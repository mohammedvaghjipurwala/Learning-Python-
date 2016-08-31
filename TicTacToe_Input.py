game = [[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]]

i = 1
def PrintMat(game):
    return ('\n'.join(str(i) for i in game))
    
def TicTacToeInput(game,i):
    if any(0 in s for s in game):
        if i % 2 != 0:
            Player = "X"
        else:
            Player = "O"
        
        print ("\nPlayer ",Player," Turn!!! \n")
        row = int(input("Enter the row (1-3): ")) - 1
        col = int(input("Enter the column (1-3): ")) - 1
        if game[row][col] == 0:
            game[row][col] = Player
            i += 1
            print (PrintMat(game))
            TicTacToeInput(game,i)
        else:
            print ("Invalid position please Try again")
            TicTacToeInput(game,i)
            
if __name__ == "__main__":
    print ("Welcome to the Tic Tac Toe game !!!")
    TicTacToeInput(game,i)
