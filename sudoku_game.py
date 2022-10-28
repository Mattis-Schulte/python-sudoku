from copy import deepcopy
from board_generation import SudokuBoard
from os import system, name
from time import time


class SudokuGame(SudokuBoard):
    identifier = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I')

    def __init__(self):
        super().__init__()
        self.solution = deepcopy(self.board)

    def print_board(self, _board):
        # print the column identifier
        print('\033[34m  1 2 3   4 5 6   7 8 9\033[0m')

        for i in range(len(_board)):
            # print the row identifier
            print(f'\033[34m{self.identifier[i]} \033[0m', end='')
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

    def play(self, difficulty):
        # puncture the board which was generated by the parent class
        self.board = self.puncture_board(self.board, difficulty)

        invalid_input = False
        number_of_mistakes = 0
        start_time = time()

        while True:
            system('cls' if name == 'nt' else 'clear')
            self.print_board(self.board)
            print('\nEnter the position (row, column) and the number you want to insert separated by a space.')
            print('Enter "exit" to quit.\n')

            if invalid_input:
                print('Invalid input. Please try again.')

            user_input = input('Enter your input: ')

            if user_input == 'exit':
                break

            try:
                user_input = user_input.split()
                row = self.identifier.index(str(user_input[0][0]).upper())
                column = int(user_input[0][1]) - 1

                # check if the input is valid
                if self.board[row][column] == 0:
                    # check if the input is correct
                    if self.solution[row][column] == int(user_input[1]):
                        self.board[row][column] = int(user_input[1])
                        invalid_input = False
                        # check if the board is complete
                        if self.board == self.solution:
                            system('cls' if name == 'nt' else 'clear')
                            self.print_board(self.board)
                            print('\nCongratulations! You solved the board!')
                            elapsed_time = round(time() - start_time)
                            print(f'Mistakes: {number_of_mistakes}, Time: {elapsed_time // 60}:{str(elapsed_time % 60).zfill(2)}')
                            break
                    else:
                        number_of_mistakes += 1
                        invalid_input = True
                else:
                    invalid_input = True
            except (ValueError, IndexError):
                invalid_input = True


if __name__ == '__main__':
    system('cls' if name == 'nt' else 'clear')
    # difficulty settings
    difficulty_levels = {'1': 25, '2': 35, '3': 45}

    # difficulty level menu
    print('''
███████╗██╗   ██╗██████╗  ██████╗ ██╗  ██╗██╗   ██╗
██╔════╝██║   ██║██╔══██╗██╔═══██╗██║ ██╔╝██║   ██║
███████╗██║   ██║██║  ██║██║   ██║█████╔╝ ██║   ██║
╚════██║██║   ██║██║  ██║██║   ██║██╔═██╗ ██║   ██║
███████║╚██████╔╝██████╔╝╚██████╔╝██║  ██╗╚██████╔╝
    ''')
    print('Welcome to Sudoku!')
    usr_input = input('Please choose the difficulty level (1: easy, 2: medium, 3: hard): ')

    while usr_input not in ('1', '2', '3'):
        print('Invalid input. Please try again.')
        usr_input = input('>> ')

    game = SudokuGame()
    game.play(difficulty_levels[usr_input])
