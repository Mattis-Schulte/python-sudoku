from random import shuffle
from timeit import timeit


class BoardFactorySimple:
    def __init__(self):
        self.board = self.generate_board()

    @staticmethod
    def generate_board():
        base_grid = list(range(1, 10))
        shuffle(base_grid)

        _board = []
        for i in range(3):
            for j in range(3):
                _board.append(base_grid[i + j * 3:] + base_grid[:i + j * 3])

        return _board

    @staticmethod
    def print_board(_board):
        for i in range(len(_board)):
            if i % 3 == 0 and i != 0:
                print('------+-------+------')

            for j in range(len(_board[0])):
                if j % 3 == 0 and j != 0:
                    print('| ', end='')

                if _board[i][j] == 0:
                    output_value = ' '
                else:
                    output_value = _board[i][j]

                if j == 8:
                    print(output_value)
                else:
                    print(f'{output_value} ', end='')


if __name__ == '__main__':
    board = BoardFactorySimple()
    board.print_board(board.board)

    number_of_runs = 1000000
    total_time = timeit(lambda: BoardFactorySimple(), number=number_of_runs)
    print(f'\nGenerated {number_of_runs} boards in {total_time} seconds, average time per board: {total_time / number_of_runs} seconds')
