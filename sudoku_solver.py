#Sudoku Solver

#===================
#Constants:

sudoku_board = [
    [0,4,7,0,8,1,0,6,3],
    [0,2,1,9,0,0,8,4,5],
    [6,8,9,0,0,0,2,0,7],
    [0,0,0,0,7,0,8,0,0],
    [7,5,0,0,3,2,0,0,0],
    [9,2,0,0,0,0,0,0,3],
    [4,9,0,7,0,0,0,2,0],
    [0,0,0,0,0,4,5,0,0],
    [1,0,2,8,3,0,0,0,0]
    ]
#Sudoku Board Drawn
# 0 4 7 | 0 2 1 | 6 8 9
# 0 8 1 | 9 0 0 | 0 0 0
# 0 6 3 | 8 4 5 | 2 0 7
#-----------------------
# 0 0 0 | 7 5 0 | 9 2 0
# 0 7 0 | 0 3 2 | 0 0 0
# 8 0 0 | 0 0 0 | 0 0 3
#-----------------------
# 4 9 0 | 0 0 0 | 1 0 2
# 7 0 0 | 0 0 4 | 8 3 0
# 0 2 0 | 5 0 0 | 0 0 0

#===================
#Data Definitions:

#test_number is integer (1 to 9)
#This is the current tested number
#Examples
test_number1 = 1 #first tested number
test_number2 = 5 #middle tested number
test_number3 = 9 #last tested number

#current_sudoku_board is list of lists
#This is a list of lists which represents the sudoku board.
#Each inner list represents a 3x3 square on the board
#Zero values represent an empty cell

#Example Starting Board:
# 0 4 7 | 0 2 1 | 6 8 9
# 0 8 1 | 9 0 0 | 0 0 0
# 0 6 3 | 8 4 5 | 2 0 7
#-----------------------
# 0 0 0 | 7 5 0 | 9 2 0
# 0 7 0 | 0 3 2 | 0 0 0
# 8 0 0 | 0 0 0 | 0 0 3
#-----------------------
# 4 9 0 | 0 0 0 | 1 0 2
# 7 0 0 | 0 0 4 | 8 3 0
# 0 2 0 | 5 0 0 | 0 0 0
current_sudoku_board1 = [ #first test in first cell
    [1,4,7,0,8,1,0,6,3],
    [0,2,1,9,0,0,8,4,5],
    [6,8,9,0,0,0,2,0,7],
    [0,0,0,0,7,0,8,0,0],
    [7,5,0,0,3,2,0,0,0],
    [9,2,0,0,0,0,0,0,3],
    [4,9,0,7,0,0,0,2,0],
    [0,0,0,0,0,4,5,0,0],
    [1,0,2,8,3,0,0,0,0]
    ]

current_sudoku_board2 = [ #middle test
    [5,4,7,2,8,1,9,6,3],
    [3,2,1,9,7,6,8,4,5],
    [6,8,9,3,5,4,2,1,7],
    [6,3,4,1,7,9,8,5,2],
    [7,5,8,4,3,2,1,6,9],
    [9,2,1,3,0,0,0,0,3],
    [4,9,0,7,0,0,0,2,0],
    [0,0,0,0,0,4,5,0,0],
    [1,0,2,8,3,0,0,0,0]
    ]

current_sudoku_board3 = [ #final completed board
    [5,4,7,2,8,1,9,6,3],
    [3,2,1,9,7,6,8,4,5],
    [6,8,9,3,5,4,2,1,7],
    [6,3,4,1,7,9,8,5,2],
    [7,5,8,4,3,2,1,6,9],
    [9,2,1,5,6,8,7,4,3],
    [4,9,5,7,1,6,3,2,8],
    [6,8,3,2,9,4,5,1,7],
    [1,7,2,8,3,5,4,9,6]
    ]
#Answer
# 5 4 7 | 3 2 1 | 6 8 9
# 2 8 1 | 9 7 6 | 3 5 4
# 9 6 3 | 8 4 5 | 2 1 7
#-----------------------
# 6 3 4 | 7 5 8 | 9 2 1
# 1 7 9 | 4 3 2 | 5 6 8
# 8 5 2 | 1 6 9 | 7 4 3
#-----------------------
# 4 9 5 | 6 8 3 | 1 7 2
# 7 1 6 | 2 9 4 | 8 3 5
# 3 2 8 | 5 1 7 | 4 9 6





#Algorithm
#Take initial Board
#Find first instance of Zero
#add 1 to cell
#if 3x3, row and column are all fine, move to next cell and add 1...
#if not, add 1 to cell. Repeat above
#if number gets to 9 without resolution, go to previous number and add 1
