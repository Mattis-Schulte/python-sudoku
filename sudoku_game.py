from board_generation import SudokuBoard
from os import system, name
from time import time

if name == 'nt':
    clear_cmd = 'system("cls")'
else:
    clear_cmd = 'system("clear")'

class SudokuGame(SudokuBoard):
    identifier = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I')

    def __init__(self):
        super().__init__()
        # puncture the board which was generated by the parent class
        self.punctured_board = self.generate_holes(35)

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

    def play(self):
        invalid_input = False
        number_of_mistakes = 0
        start_time = time()

        while True:
            exec(clear_cmd)
            self.print_board(self.punctured_board)
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

                # check if the input is correct
                if self.punctured_board[row][column] == 0:
                    if self.board[row][column] == int(user_input[1]):
                        self.punctured_board[row][column] = int(user_input[1])
                        invalid_input = False
                        # check if the board is complete
                        if self.punctured_board == self.board:
                            exec(clear_cmd)
                            self.print_board(self.punctured_board)
                            print(f'\nYou won with {number_of_mistakes} mistake in {round(time() - start_time, 2)} seconds.')
                            break
                    number_of_mistakes += 1
                invalid_input = True
            except (ValueError, IndexError):
                # input error
                invalid_input = True

if __name__ == '__main__':
    game = SudokuGame()
    game.play()