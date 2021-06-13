#Sudoku Solver
#===================
#Constants:

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


# 5 4 7 | 3 2 1 | 6 8 9

sudoku_board = [
    5,4,7,0,8,1,0,6,3,
    0,2,1,9,0,0,8,4,5,
    6,8,9,0,0,0,2,0,7,
    0,0,0,0,7,0,8,0,0,
    7,5,0,0,3,2,0,0,0,
    9,2,0,0,0,0,0,0,3,
    4,9,0,7,0,0,0,2,0,
    0,0,0,0,0,4,5,0,0,
    1,0,2,8,3,0,0,0,0
    ]


sudoku_board1 = [
    1,4,7,1,8,1,1,6,3,
    0,2,1,9,0,0,8,4,5,
    6,8,9,0,0,0,2,0,7,
    0,0,0,0,7,0,8,0,0,
    7,5,0,0,3,2,0,0,0,
    9,2,0,0,0,0,0,0,3,
    4,9,0,7,0,0,0,2,0,
    0,0,0,0,0,4,5,0,0,
    1,0,2,8,3,0,0,0,0
    ]
sudoku_board2 = [
    1,4,7,0,8,1,0,6,3,
    0,2,1,9,0,0,8,4,5,
    6,8,9,0,0,0,2,0,7,
    0,0,0,0,7,0,8,0,0,
    7,5,0,0,3,2,0,0,0,
    9,2,0,0,0,0,0,0,3,
    4,9,0,7,0,0,0,2,0,
    0,0,0,0,0,4,5,0,0,
    1,0,2,8,3,0,0,0,0
    ]
sudoku_board3 = [ #final completed board
     5,4,7,2,8,1,9,6,3,
     3,2,1,9,7,6,8,4,5,
     6,8,9,3,5,4,2,1,7,
     6,3,4,1,7,9,8,5,2,
     7,5,8,4,3,2,1,6,9,
     9,2,1,5,6,8,7,4,3,
     4,9,5,7,1,6,3,2,8,
     6,8,3,2,9,4,5,1,7,
     1,7,2,8,3,5,4,9,6
     ]

#===================
#Data Definitions:

#test_number is integer (1 to 9)
#This is the current tested number
#Examples
# test_number1 = 1 #first tested number
# test_number2 = 5 #middle tested number
# test_number3 = 9 #last tested number

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
# current_sudoku_board1 = [ #first test in first cell
#     [1,4,7,0,8,1,0,6,3],
#     [0,2,1,9,0,0,8,4,5],
#     [6,8,9,0,0,0,2,0,7],
#     [0,0,0,0,7,0,8,0,0],
#     [7,5,0,0,3,2,0,0,0],
#     [9,2,0,0,0,0,0,0,3],
#     [4,9,0,7,0,0,0,2,0],
#     [0,0,0,0,0,4,5,0,0],
#     [1,0,2,8,3,0,0,0,0]
#     ]
#
# current_sudoku_board2 = [ #middle test
#     [5,4,7,2,8,1,9,6,3],
#     [3,2,1,9,7,6,8,4,5],
#     [6,8,9,3,5,4,2,1,7],
#     [6,3,4,1,7,9,8,5,2],
#     [7,5,8,4,3,2,1,6,9],
#     [9,2,1,3,0,0,0,0,3],
#     [4,9,0,7,0,0,0,2,0],
#     [0,0,0,0,0,4,5,0,0],
#     [1,0,2,8,3,0,0,0,0]
#     ]
#
# current_sudoku_board3 = [ #final completed board
#     [5,4,7,2,8,1,9,6,3],
#     [3,2,1,9,7,6,8,4,5],
#     [6,8,9,3,5,4,2,1,7],
#     [6,3,4,1,7,9,8,5,2],
#     [7,5,8,4,3,2,1,6,9],
#     [9,2,1,5,6,8,7,4,3],
#     [4,9,5,7,1,6,3,2,8],
#     [6,8,3,2,9,4,5,1,7],
#     [1,7,2,8,3,5,4,9,6]
#     ]
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


#===================
#Functions:

def is_within_sudoku_rules(input):
    # make it >0
    natural_numbers_list = list(filter(lambda x: x > 0, input))
    # remove duplicates
    set_list = list(set(natural_numbers_list))
    # if natural_numbers_list == set_list, no natural numbers duplicates
    return natural_numbers_list == set_list

#Find next instance of Zero
def find_zero(csb):
    #Find next instance of Zero
    #Input = current sudoku Board
    #Output = index position of next zero, where zero is at sudoku_board[Output]
    if 0 in csb:
        index = csb.index(0)
        return(index)
    else:
        return(999)

def check_square(current_index, sudoku_board):
    #Function that takes the current index and current sudoku board and outputs
    #a boolean stating whether the rules have been met (True) or not (False)
    remainder = current_index % 9
    #take numbers either side - determined by remainder
    square_list = [sudoku_board[i] for i in list(range(current_index-remainder, current_index+(9-remainder)))]
    #check if rules have been met
    return(is_within_sudoku_rules(square_list))

def check_row(current_index, sudoku_board):
    init_row_index_num = [ 0,1,2,9,10,11,18,19,20]
    remainder = current_index % 9

    if remainder in [0,1,2] and current_index<=26:
        row_index_num = [x+0 for x in init_row_index_num]
    elif remainder in [0,1,2] and current_index <=53:
        row_index_num = [x+27 for x in init_row_index_num]
    elif remainder in [0,1,2]:
        row_index_num = [x+54 for x in init_row_index_num]
    elif remainder in [3,4,5] and current_index<=26:
        row_index_num = [x+3 for x in init_row_index_num]
    elif remainder in [3,4,5] and current_index <=53:
        row_index_num = [x+30 for x in init_row_index_num]
    elif remainder in [3,4,5]:
        row_index_num = [x+57 for x in init_row_index_num]
    elif remainder in [6,7,8] and current_index<=26:
        row_index_num = [x+6 for x in init_row_index_num]
    elif remainder in [6,7,8] and current_index<=53:
        row_index_num = [x+33 for x in init_row_index_num]
    elif remainder in [6,7,8]:
        row_index_num = [x+60 for x in init_row_index_num]

    row_list = [sudoku_board[i] for i in row_index_num]

    return(is_within_sudoku_rules(row_list))

def check_col(current_index, sudoku_board):

    #get index of number calculate remainder of index when divided by 9
    remainder_27 = current_index % 27

    #index numbers for columns
    if remainder_27 in [0,3,6]:
        col_index_num = [ 0,  3,  6, 27, 30, 33, 54, 57, 60]
    elif remainder_27 in [1,4,7]:
        col_index_num = [ 1,  4,  7, 28, 31, 34, 55, 58, 61]
    elif remainder_27 in [2,5,8]:
        col_index_num = [ 2,  5,  8, 29, 32, 35, 56, 59, 62]
    elif remainder_27 in [9,12,15]:
        col_index_num = [ 9, 12, 15, 36, 39, 42, 63, 66, 69]
    elif remainder_27 in [10,13,16]:
        col_index_num = [10, 13, 16, 37, 40, 43, 64, 67, 70]
    elif remainder_27 in [11,14,17]:
        col_index_num = [11, 14, 17, 38, 41, 44, 65, 68, 71]
    elif remainder_27 in [18,21,24]:
        col_index_num = [18, 21, 24, 45, 48, 51, 72, 75, 78]
    elif remainder_27 in [19,22,25]:
        col_index_num = [19, 22, 25, 46, 49, 52, 73, 76, 79]
    elif remainder_27 in [20,23,26]:
        col_index_num = [20, 23, 26, 47, 50, 53, 74, 77, 80]

    col_list = [sudoku_board[i] for i in col_index_num]

    #check if rules have been met
    return(is_within_sudoku_rules(col_list))
#===================
#Algorithm:
#Take initial Board

current_index = find_zero(sudoku_board)

#add 1 to cell
sudoku_board[current_index] += 1

#check rules are met
#Identify which 3x3 to check
#find remainder of index
square_rules_met = check_square(current_index, sudoku_board)

#Identify which row to check
row_rules_met = check_row(current_index, sudoku_board)

#identify which column to check
col_rules_met = check_col(current_index, sudoku_board)
#Check rules met for 3x3, row and column
rules_met = square_rules_met and row_rules_met and col_rules_met

#if 3x3, row and column are all fine, move to next cell and add 1...
#if rules met, move to next cell


#if not, add 1 to cell. Repeat above





#if number gets to 9 without resolution, go to previous number and add 1
