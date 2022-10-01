from random import shuffle
from copy import deepcopy


class SudokuBoard:
    def __init__(self):
        self.board = self.generate_board()

    # generate the board
    def generate_board(self):
        _board = [[0 for _ in range(9)] for _ in range(9)]
        self.fill_board(_board)
        return _board

    # fill the board
    def fill_board(self, _board):    
        find = self.find_empty(_board)
        if not find:
            return True
        else:
            row, col = find
        
        nums = list(range(1, 10))
        shuffle(nums)

        for i in nums:
            if self.validate_entry(_board, i, (row, col)):
                _board[row][col] = i

                # fill the next empty cell recursively
                if self.fill_board(_board):
                    return True

                # if the next cell is impossible to fill, backtrack
                _board[row][col] = 0

        return False

    # find an empty position
    @staticmethod
    def find_empty(_board):
        for i in range(len(_board)):
            for j in range(len(_board[0])):
                if _board[i][j] == 0:
                    return i, j  # row, col

        return None

    # check if the number is valid in the position
    @staticmethod
    def validate_entry(_board, num, pos):
        # check row
        if num in _board[pos[0]]:
            return False

        # check column
        for i in range(len(_board)):
            if _board[i][pos[1]] == num:
                return False

        # check box
        box_x = pos[1] // 3
        box_y = pos[0] // 3

        if any(num in row[box_x * 3:box_x * 3 + 3] for row in _board[box_y * 3:box_y * 3 + 3]):
            return False

        return True

    # remove random numbers
    def puncture_board(self, holes):
        _board = deepcopy(self.board)
        positions = list(range(81))
        shuffle(positions)

        for i in range(holes):
            row = positions[i] // 9
            col = positions[i] % 9
            _board[row][col] = 0

        return _board
