from random import shuffle
import numpy as np
from timeit import timeit


class BoardFactory:
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
            if self.valid_entry(_board, i, (row, col)):
                _board[row][col] = i

                if self.fill_board(_board):
                    return True

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
    def valid_entry(_board, num, pos):
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

    # print the board
    def print_board(self):
        for i in range(len(self.board)):
            if i % 3 == 0 and i != 0:
                print('------+-------+------')

            for j in range(len(self.board[0])):
                if j % 3 == 0 and j != 0:
                    print('| ', end='')

                if j == 8:
                    print(self.board[i][j])
                else:
                    print(str(self.board[i][j]) + ' ', end='')


if __name__ == '__main__':
    board = BoardFactory()
    # board.print_board()
    number_of_runs = 10000
    total_time = timeit(lambda: board.generate_board(), number=number_of_runs)
    print(f'Generated {number_of_runs} boards in {total_time} seconds, average time per board: {total_time / number_of_runs} seconds')
