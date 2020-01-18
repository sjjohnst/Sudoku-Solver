import math

def printBoard(board):
    for row in board:
        print(row)

def validInput(row, col, board, entry):
    #Check row
    if(entry in board[row]):
       return False

    #Check column
    for eachRow in range(9):
        if(entry == board[eachRow][col]):
            return False

    #Determine the index of current Box Corner
    verticalBoxIndex = math.trunc(row / 3)
    horizontalBoxIndex = math.trunc(col / 3)

    cornerRow = 3 * verticalBoxIndex
    cornerCol = 3 * horizontalBoxIndex

    #Check box
    for i in range(3):
        for j in range(3):
            if(entry == board[cornerRow + i][cornerCol + j]):
                return False

    return True

def solve(row, col, board):

    #Return true
    if(col == len(board[row])):

        col = 0
        row += 1
        
        if(row == len(board)):
            return True

    if(board[row][col] != 0):
        return solve(row, col+1, board)

    #Possible entries for current cell
    for x in range(1,10):
        
        if(validInput(row, col, board, x)):
            board[row][col] = x
            #Recursion (move to next cell)
            if(solve(row, col+1, board)):
                return True
            #Board does not get solved, backtrack and try new value
            board[row][col] = 0

    #board is unsolvable
    return False
    

def solveSudoku(board):
    if solve(0,0,board):
        #printBoard(board)
        pass

'''
Next step: User interface, allowing them to input their own sudoku board


sudoku = [[0, 0, 4, 6, 7, 0, 0, 2, 0],
          [0, 0, 1, 2, 0, 9, 0, 8, 6],
          [0, 0, 0, 0, 8, 0, 0, 5, 0],
          [0, 0, 9, 0, 0, 0, 0, 6, 3],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [1, 8, 0, 0, 0, 0, 5, 0, 0],
          [0, 1, 0, 0, 3, 0, 0, 0, 0],
          [4, 9, 0, 7, 0, 8, 2, 0, 0],
          [0, 3, 0, 0, 4, 5, 6, 0, 0]]

printBoard(sudoku)

solveSudoku(sudoku)
'''

