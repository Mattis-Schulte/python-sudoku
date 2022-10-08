from random import shuffle
from timeit import timeit
from copy import deepcopy


class SudokuBoard:
    def __init__(self):
        self.board = self.generate_board()
        # self.punctured_board = self.puncture_board(40)

    # generate the board
    def generate_board(self) -> list:
        _board = [[0 for _ in range(9)] for _ in range(9)]
        self.fill_board(_board)
        return _board

    # fill the board
    def fill_board(self, _board: list, selected_cell: int=0) -> bool:
        nums = list(range(1, 10))
        shuffle(nums)

        # check if the board is already complete
        if selected_cell == 81:
            return True

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


if __name__ == '__main__':
    board = SudokuBoard()
    board.print_board(board.board)
    # print()
    # board.print_board(board.punctured_board)

    number_of_runs = 10000
    total_time = timeit(lambda: SudokuBoard(), number=number_of_runs)
    print(f'\nGenerated {number_of_runs} boards in {total_time} seconds, average time per board: {total_time / number_of_runs} seconds')
    