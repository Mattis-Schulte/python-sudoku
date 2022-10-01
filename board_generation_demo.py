from random import shuffle, randint
from timeit import timeit
from copy import deepcopy


class SudokuBoard:
    def __init__(self):
        self.board = self.generate_board()
        self.punctured_board = self.generate_holes(40)

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

                # next cell is impossible to fill, backtrack
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
    def generate_holes(self, holes):
        _board = deepcopy(self.board)
        positions = list(range(81))
        shuffle(positions)

        for i in range(holes):
            row = positions[i] // 9
            col = positions[i] % 9
            _board[row][col] = 0

        return _board

    # print the board
    def print_board(self, _board):
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

if __name__ == '__main__':
    board = SudokuBoard()
    board.print_board(board.board)
    print()
    board.print_board(board.punctured_board)

    number_of_runs = 10000
    total_time = timeit(lambda: SudokuBoard(), number=number_of_runs)
    print(f'\nGenerated {number_of_runs} boards in {total_time} seconds, average time per board: {total_time / number_of_runs} seconds')
    