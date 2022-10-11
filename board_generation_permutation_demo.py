"""
Simple demo of a permutation algorithm
Runtime for a single board: 0.2 milliseconds (measured on GitHub Codespaces)
Source: https://stackoverflow.com/a/61442050/12278623
"""

from random import randint, shuffle
from timeit import timeit
from copy import deepcopy


class BoardFactoryExample:
    def __init__(self):
        self.board = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [4, 5, 6, 7, 8, 9, 1, 2, 3], [7, 8, 9, 1, 2, 3, 4, 5, 6],
                      [2, 3, 1, 5, 6, 4, 8, 9, 7], [5, 6, 4, 8, 9, 7, 2, 3, 1], [8, 9, 7, 2, 3, 1, 5, 6, 4],
                      [3, 1, 2, 6, 4, 5, 9, 7, 8], [6, 4, 5, 9, 7, 8, 3, 1, 2], [9, 7, 8, 3, 1, 2, 6, 4, 5]]
        self.generate_board()
        # self.punctured_board = self.puncture_board(40)

    def swap_numbers(self, n1: int, n2: int):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == n1:
                    self.board[i][j] = n2
                elif self.board[i][j] == n2:
                    self.board[i][j] = n1

    def swap_rows(self, r1: int, r2: int):
        self.board[r1], self.board[r2] = self.board[r2], self.board[r1]

    def swap_cols(self, c1: int, c2: int):
        for i in range(9):
            self.board[i][c1], self.board[i][c2] = self.board[i][c2], self.board[i][c1]

    def swap_3x3_rows(self, r1: int, r2: int):
        for i in range(3):
            self.swap_rows(r1 * 3 + i, r2 * 3 + i)

    def swap_3x3_cols(self, c1: int, c2: int):
        for i in range(3):
            self.swap_cols(c1 * 3 + i, c2 * 3 + i)

    def shuffle_numbers(self):
        for i in range(1, 10):
            ran_num = randint(1, 9)
            self.swap_numbers(i, ran_num)

    def shuffle_cols(self):
        for i in range(9):
            ran_num = randint(0, 2)
            self.swap_cols(i, i // 3 * 3 + ran_num)

    def shuffle_3x3_rows(self):
        for i in range(3):
            ran_num = randint(0, 2)
            self.swap_3x3_rows(i, ran_num)

    def shuffle_3x3_cols(self):
        for i in range(3):
            ran_num = randint(0, 2)
            self.swap_3x3_cols(i, ran_num)

    def generate_board(self):
        self.shuffle_numbers()
        self.shuffle_cols()
        self.shuffle_3x3_rows()
        self.shuffle_3x3_cols()
    
    # remove random numbers
    def puncture_board(self, holes: int) -> list:
        _board = deepcopy(self.board)
        positions = list(range(81))
        shuffle(positions)

        for i in range(holes):
            row = positions[i] // 9
            col = positions[i] % 9
            _board[row][col] = 0

        return _board

    # print the board
    @staticmethod
    def print_board(_board: list):
        identifier = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I')
        # print the column identifier
        print('\033[34m  1 2 3   4 5 6   7 8 9\033[0m')
    
        for i in range(len(_board)):
            # print the row identifier
            print(f'\033[34m{identifier[i]} \033[0m', end='')
            for j in range(len(_board[0])):
                if j % 3 == 0 and j != 0:
                    print('| ', end='')

                # print the number if it's not 0
                if _board[i][j] == 0:
                    output_value = ' '
                else:
                    output_value = _board[i][j]

                if j == 8:
                    print(output_value)
                else:
                    print(f'{output_value} ', end='')
            # print the row separator
            if i % 3 == 2 and i != 8:
                print('  ------+-------+------')


if __name__ == "__main__":
    board = BoardFactoryExample()
    board.print_board(board.board)
    # print()
    # board.print_board(board.punctured_board)

    number_of_runs = 10000
    total_time = timeit(lambda: BoardFactoryExample(), number=number_of_runs)
    print(f'\nGenerated {number_of_runs} boards in {total_time} seconds, average time per board: {total_time / number_of_runs} seconds')
