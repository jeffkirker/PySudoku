import pprint as pp
import math


# Check if given value exists in the row
def check_in_row(board, row, num):
    for i in board[row]:
        if i == num:
            return True
    return False

# Check if given value exists in col
def check_in_col(board, col, num):
    for i in range(0,9):
        if board[i][col] == num:
            return True
    return False

# Check if given value exists in 3x3 subgrid
def check_in_subgrid(board, row, col, num):
    row_start = row - row%3
    col_start = col - col%3
    for i in range(row_start, row_start+3):
        for j in range(col_start, col_start+3):
            if board[i][j] == num:
                return True
    return False
    
# Overall check if number is valid
def valid_num(board, row, col, num):
    if check_in_col(board, col, num) == True:
        return False
    if check_in_row(board, row, num) == True:
        return False
    if check_in_subgrid(board, row, col, num) == True:
        return False
    return True

# Get the next empty cell
def get_empty(board):
    for i in range(0, 9):
        for j in range(0, 9):
            if board[i][j] == 0:
                return i, j
    
def empty_exists(board):
    for i in range(0, 9):
        for j in range(0, 9):
            if board[i][j] == 0:
                return True
    return False

def solve_sudoku(board):
    if not empty_exists(board):
        return board
    
    row, col = get_empty(board)
    
    for i in range(0,10):
        if valid_num(board, row, col, i):
            board[row][col] = i

            if(solve_sudoku(board)):
                return board
            
            board[row][col] = 0

    return False




def main():
    board = [[3, 0, 6, 5, 0, 8, 4, 0, 0],  
    [5, 2, 0, 0, 0, 0, 0, 0, 0],  
    [0, 8, 7, 0, 0, 0, 0, 3, 1],  
    [0, 0, 3, 0, 1, 0, 0, 8, 0],  
    [9, 0, 0, 8, 6, 3, 0, 0, 5],  
    [0, 5, 0, 0, 9, 0, 6, 0, 0],  
    [1, 3, 0, 0, 0, 0, 2, 5, 0],  
    [0, 0, 0, 0, 0, 0, 0, 7, 4],  
    [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    board_solved = solve_sudoku(board)
    
    pp.pprint(board_solved)

main()