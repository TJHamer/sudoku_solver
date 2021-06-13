#Sudoku Solver
#A program to solve a sudoku puzzle
#Enter a sudoku puzzle, run code and it will produce an output of a list of numbers
#which can be interpreted as the final result
#===================
#Constants:
#Example Starting Board:
# a1 a2 a3 | a4 a5 a6 | a7 a8 a9
# b1 b2 b3 | b4 b5 b6 | b7 b8 b9
# c1 c2 c3 | c4 c5 c6 | c7 c8 c9
#---------------------------------
# d1 d2 d3 | d4 d5 d6 | d7 d8 d9
# e1 e2 e3 | e4 e5 e6 | e7 e8 e9
# f1 f2 f3 | f4 f5 f6 | f7 f8 f9
#---------------------------------
# g1 g2 g3 | g4 g5 g6 | g7 g8 g9
# h1 h2 h3 | h4 h5 h6 | h7 h8 h9
# i1 i2 i3 | i4 i5 i6 | i7 i8 i9

#sudoku_board is list of numbers
#This is a list of numbers which represents the sudoku board.
#Zero values represent an empty cell
#Each row below, or every 9 numbers of list, represent 1 3x3 square of the sudoku puzzle
#the numbers go from top left to bottom right of each 3x3 square, then top left to bottom right of puzzle
# sudoku_board = [
#   a1,a2,a3,b1,b2,b3,c1,c2,c3,
#   a4,a5,a6,b4,b5,b6,c4,c5,c6,
#   a7,a8,a9,b7,b8,b9,c7,c8,c9,
#   d1,d2,d3,e1,e2,e3,f1,f2,f3,
#   d4,d5,d6,e4,e5,e6,f4,f5,f6,
#   d7,d8,d9,e7,e8,e9,f7,f8,f9,
#   g1,g2,g3,h1,h2,h3,i1,i2,i3,
#   g4,g5,g6,h4,h5,h6,i4,i5,i6,
#   g7,g8,g9,h7,h8,h9,i7,i8,i9,
#     ]

sudoku_board = [
    3,0,5,4,9,0,6,0,0,
    4,0,2,7,6,0,1,0,3,
    0,6,0,1,0,8,2,4,5,
    0,0,3,9,6,0,0,8,1,
    9,0,0,0,5,8,3,0,4,
    5,8,0,7,0,3,0,9,2,
    0,5,0,2,0,0,1,4,9,
    6,0,1,5,4,9,0,0,7,
    4,0,0,0,7,0,3,0,6
    ]
#===================

#Functions:

def is_within_sudoku_rules(list_of_numbers):
    #function to determine whether a list of numbers meets the sudoku rule criteria
    #of all numbers from 1-9 being unique (zeros not included)
    #Input: List of numbers
    #Output: Boolean
    natural_numbers_list = list(filter(lambda x: x > 0, list_of_numbers)) #list of natural numbers
    set_list = list(set(natural_numbers_list)) # remove duplicates
    # if length of natural_numbers_list == length of set_list, no natural numbers duplicates
    return len(natural_numbers_list) == len(set_list)

def check_square(current_index, sudoku_board):
    #States whether the sudoku rules have been met in a 3x3 square
    #Input: current_index as Number, sudoku_board as list of list_of_numbers
    #Output: Boolean
    remainder = current_index % 9
    #take numbers either side - determined by remainder
    first_index = current_index-remainder
    last_index = current_index+(9-remainder)
    square_list = [sudoku_board[i] for i in list(range(first_index, last_index))]
    #check if rules have been met
    return(is_within_sudoku_rules(square_list))

def check_row(current_index, sudoku_board):
    #States whether the sudoku rules have been met in a row
    #Input: current_index as Number, sudoku_board as list of list_of_numbers
    #Output: Boolean
    init_row_index_num = [0,1,2,9,10,11,18,19,20]
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
    #States whether the sudoku rules have been met in a column
    #Input: current_index as Number, sudoku_board as list of list_of_numbers
    #Output: Boolean

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
#Find all zero cells
zero_cells = [i for i, e in enumerate(sudoku_board) if e == 0]

not_complete = True #Process isn't complete, when it is this changes to False and process ends
current_zero_index = 0 #Index for zero/unknown number list

while not_complete:
    current_index = zero_cells[current_zero_index]

    sudoku_board[current_index] += 1 #add 1 to cell

    #check rules are met
    square_rules_met = check_square(current_index, sudoku_board)     #3x3
    row_rules_met    = check_row(current_index, sudoku_board)        #row
    col_rules_met    = check_col(current_index, sudoku_board)        #column
    rules_met = square_rules_met and row_rules_met and col_rules_met #combined

    #If rules met...
    if rules_met:
        #check if finished.
        if current_index == max(zero_cells):
            not_complete = False
        #If not finished, move to next cell.
        else:
            current_zero_index += 1
    #If rules not met...
    else:
        #check if value is 9. If 9, make zero and move to previous number (current_zero_index - 1)
        if sudoku_board[current_index] == 9:
            sudoku_board[current_index] = 0
            current_zero_index -= 1
        #If not 9, leave things as is and repeat steps above

print(sudoku_board)
