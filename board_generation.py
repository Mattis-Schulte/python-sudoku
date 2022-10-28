from random import shuffle
from copy import deepcopy


class SudokuBoard:
    def __init__(self):
        self.board = self.generate_board()

    # generate the board
    def generate_board(self) -> list:
        _board = [[0 for _ in range(9)] for _ in range(9)]
        self.fill_board(_board)
        return _board

    # fill the board
    def fill_board(self, _board: list, selected_cell: int=0) -> bool:   
        # check if the board is already complete
        if selected_cell == 81:
            return True

        nums = list(range(1, 10))
        shuffle(nums)

        for i in nums:
            selected_row = selected_cell // 9
            selected_col = selected_cell % 9

            if self.validate_entry(_board, i, (selected_row, selected_col)):
                _board[selected_row][selected_col] = i

                # fill the next empty cell recursively
                if self.fill_board(_board, selected_cell + 1):
                    return True

                # if the next cell is impossible to fill, backtrack
                _board[selected_row][selected_col] = 0

        return False

    # check if the number is valid in this position
    @staticmethod
    def validate_entry(_board: list, num: int, pos: tuple) -> bool:
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
    @staticmethod
    def puncture_board(_board, holes: int) -> list:
        positions = list(range(81))
        shuffle(positions)

        for i in range(holes):
            row = positions[i] // 9
            col = positions[i] % 9
            _board[row][col] = 0

        return _board
