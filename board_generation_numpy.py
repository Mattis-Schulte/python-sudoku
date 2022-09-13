from random import shuffle
import numpy as np
from time import time


class BoardFactory:
    def __init__(self):
        self.board = self.generate_board()

    # generate the board
    def generate_board(self):
        _board = np.zeros((9, 9), dtype=int)
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
        find = np.where(_board == 0)
        if len(find[0]) > 0:
            return find[0][0], find[1][0]
        else:
            return None

    # check if the number is valid in the position
    @staticmethod
    def valid_entry(_board, num, pos):
        # check row
        if num in _board[pos[0]]:
            return False

        # check column
        if num in _board[:, pos[1]]:
            return False

        # check box
        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if _board[i][j] == num and (i, j) != pos:
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
    total_time = 0

    # generate the board 10000 times and calculate the average time
    for variants in range(1, 10000 + 1):
        start = time()
        board = BoardFactory()
        end = time()
        total_time += end - start
        board.print_board()
        print()

    print(f'\nGenerated {variants} boards in {total_time} seconds, average time: {total_time / variants} seconds')
