#IMPORTS
import pygame as py
import time, sys, os, random
from pygame.locals import *
import TextBox
from Sudoku import solveSudoku


#COLORS
BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (200,200,200)
BLUE = (0,50,255)

#DISPLAY SPECS
WINDOWMULTIPLIER = 5 #Set size of display (ensures divisible by 9)
WINDOWSIZE = 90
WIDTH = WINDOWSIZE * WINDOWMULTIPLIER
HEIGHT = WINDOWSIZE * WINDOWMULTIPLIER

SQUARESIZE = int((WINDOWSIZE * WINDOWMULTIPLIER)/3) #Large squares
CELLSIZE = int(SQUARESIZE / 3)                      #Small squares

#FPS
FPS = 60




#FUNCTIONS
def drawGrid():
    #Draws an empty 9x9 sudoku board
    for x  in range(0, WIDTH, CELLSIZE):
        py.draw.line(window, GRAY, (x,0),(x,HEIGHT))
        py.draw.line(window, GRAY, (0,x),(WIDTH, x))

    for x in range(0, WIDTH, SQUARESIZE):
        py.draw.line(window, BLACK, (x,0),(x,HEIGHT))
        py.draw.line(window, BLACK, (0,x),(WIDTH, x))

def populateGrid(board):
    #Displays each element of the board (2D list) onto the grid
    x = 0
    y = 0
    for row in board:
        for elem in row:
            #Check if empty space
            if(elem == 0):
                x += CELLSIZE
                continue
            
            cellSurf = BASICFONT.render('%s' %(elem), True, BLACK)
            cellRect = cellSurf.get_rect()
            cellRect.topleft = (x,y)
            window.blit(cellSurf, cellRect)
            x += CELLSIZE

        #Reset x position, move down one row
        x = 0
        y += CELLSIZE

    return None

def initiateBoard():
    #Initializes the board (2D list) to be filled with zeroes (empty)
    board = [[0 for x in range(9)] for y in range(9)]  
    return board

def drawBox(mousex, mousey):
    #Displays box around cell nearest to users mouse
    boxx = int(((mousex*9)/WIDTH))*(CELLSIZE)
    boxy = int(((mousey*9)/HEIGHT))*(CELLSIZE)
    py.draw.rect(window, BLUE, (boxx,boxy,CELLSIZE,CELLSIZE), 2)

def isValidInput(num):
    if str.isdigit(num) and int(num) > 0 and int(num) < 10:
        return True
    return False

def getInput(x, y):
    #Get the users input, for entering values into the board

    #Get current cell position
    boxx = int(((x*9)/WIDTH))*(CELLSIZE)
    boxy = int(((y*9)/HEIGHT))*(CELLSIZE)
    
    textinput = TextBox.TextInput()
    num = ' '
    text = True

    #Input loop
    while text:
        events = py.event.get()
        for event in events:
            if event.type == py.QUIT:
                exit()
        
        if textinput.update(events):
            num = textinput.get_text()

            #Check if input is valid
            if not isValidInput(num):
                num = 0
                
            text = False

        #Display the user typing
        window.blit(textinput.get_surface(), (boxx, boxy))
        py.display.update()

    return num
        
def setNumber(mousex, mousey, board):
    #Places user's input into current cell
    row = int((mousex*9)/WIDTH)
    col = int((mousey*9)/HEIGHT)
    
    num = getInput(mousex, mousey)
    board[col][row] = num




#MAIN
def main():
    
    global fpsLock, window
    global BASICFONT, BASICFONTSIZE

    #Initialize Game
    py.init()
    window = py.display.set_mode((WIDTH, HEIGHT))
    fpsLock = py.time.Clock()
    
    BASICFONTSIZE = 30
    BASICFONT = py.font.Font('freesansbold.ttf', BASICFONTSIZE)

    py.display.set_caption('Sudoku Solver')
    
    board = initiateBoard()
    textinput = TextBox.TextInput()

    #Game Loop
    while True:

        mouseClicked = False
        
        for event in py.event.get():

            if event.type == py.QUIT:
                
                py.quit()
                sys.exit()

            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True

            elif event.type == py.KEYDOWN:
                if event.key == K_SPACE:
                    #Solve the current board
                    #Cast all elements of board to int
                    board = [[int(x) for x in y] for y in board]
                    solveSudoku(board)

                if event.key == K_DELETE:
                    board = initiateBoard()

        #Input a number
        if mouseClicked == True:
            setNumber(mousex, mousey, board)

        window.fill(WHITE)
        
        drawGrid()
        populateGrid(board)
        drawBox(mousex, mousey)
        
        py.display.update()
        fpsLock.tick(FPS)

main()

    
