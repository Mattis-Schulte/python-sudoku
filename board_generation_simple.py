from random import shuffle
from timeit import timeit
from copy import deepcopy


class BoardFactorySimple:
    def __init__(self):
        self.board = self.generate_board()
        # self.punctured_board = self.puncture_board(40)

    # generate the board
    @staticmethod
    def generate_board() -> list:
        base_grid = list(range(1, 10))
        shuffle(base_grid)

        _board = []
        for i in range(3):
            for j in range(3):
                _board.append(base_grid[i + j * 3:] + base_grid[:i + j * 3])

        return _board

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
    board = BoardFactorySimple()
    board.print_board(board.board)
    # print()
    # board.print_board(board.punctured_board)

    number_of_runs = 10000
    total_time = timeit(lambda: BoardFactorySimple(), number=number_of_runs)
    print(f'\nGenerated {number_of_runs} boards in {total_time} seconds, average time per board: {total_time / number_of_runs} seconds')
