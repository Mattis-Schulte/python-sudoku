import random, copy
import numpy as np

# generate a sudoku board using backtracking
def generate_board():
    board = [[0 for _ in range(9)] for _ in range(9)]
    solve(board)
    return board

# solve the sudoku board using backtracking
def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False

# check if the number is valid in the position
def valid(board, num, pos):
    # check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True

# find an empty position
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # row, col

    return None

# print the board
def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

# remove numbers from the board
def remove_numbers(board, num):
    while num > 0:
        x = random.randint(0,8)
        y = random.randint(0,8)

        if board[x][y] != 0:
            board[x][y] = 0
            num -= 1

    return board

# generate a sudoku board
def generate():
    board = generate_board()
    while not check_board(board):
        board = generate_board()
    return board

# generate a sudoku board with some numbers removed
def generate_with_holes():
    board = generate()
    board = remove_numbers(board, 40)
    return board

# solve the sudoku board
def solve_board(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve_board(board):
                return True

            board[row][col] = 0

    return False

# check if the board is solved
def check_solved(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return False
    return True

# check if the board is valid
def check_valid(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                temp = board[i][j]
                board[i][j] = 0
                if valid(board, temp, (i, j)):
                    board[i][j] = temp
                else:
                    return False
    return True

# check if the board is solved and valid
def check_board(board):
    if check_solved(board) and check_valid(board):
        return True
    return False

# game loop
def game():
    board = generate_with_holes()
    print_board(board)
    print()
    while not check_board(board):
        x = int(input("Enter row: "))
        y = int(input("Enter column: "))
        num = int(input("Enter number: "))
        if valid(board, num, (x, y)):
            board[x][y] = num
            print_board(board)
            print()
        else:
            print("Invalid number")
            print_board(board)
            print()

    print("You win!")

if __name__ == "__main__":
    game()