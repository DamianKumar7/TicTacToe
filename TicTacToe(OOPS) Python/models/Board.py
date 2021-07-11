
from math import floor

class Board:

    def __init__(self):
        self.game_board = None
        self.reset_game_board()


    def reset_game_board(self):
        self.game_board = []
        cell_number = 1
        for row in range(3):
            self.game_board.append([])
            for col in range(3):
                self.game_board[row].append(str(cell_number))
                cell_number += 1


    def show_board(self):
        for row in range(3):
            for col in range(3):
                if self.game_board[row][col] != 'X' and self.game_board[row][col] != 'O':
                    print(' _ ', end="")
                else:
                    print(' {} '.format(self.game_board[row][col]), end="")
            print()
        print()

        print(self.game_board)


    def update_board(self, position, piece):
        print(position, piece)
        for row in range(3):
            for col in range(3):
                if self.game_board[row][col] == position:
                    self.game_board[row][col] = piece


    def check_valid_position(self, position):
        for row in range(3):
            for col in range(3):
                if position == self.game_board[row][col]:
                    return True
        return False

    def get_number_of_moves_left(self):
        number_of_moves_left = 0
        for row in range(3):
            for col in range(3):
                if self.game_board[row][col] != 'X' or self.game_board[row][col] != 'O':
                    number_of_moves_left += 1

        return number_of_moves_left


    def check_diagonals_for_winner(self):
        return self.game_board[0][0] == self.game_board[1][1] == self.game_board[2][2] or self.game_board[0][2] == self.game_board[1][1] == self.game_board[2][0]

    def check_rows_for_winner(self):
        for row in range(3):
            if self.game_board[row][0] == self.game_board[row][1] == self.game_board[row][2]:
                return True

        return False

    def check_columns_for_winner(self):
        for col in range(3):
            if self.game_board[0][col] == self.game_board[1][col] == self.game_board[2][col]:
                return True

        return False


    def check_game_over(self):
        #Result Codes: 0 -> Draw, 1 -> Winner

        if  self.get_number_of_moves_left() == 0:
            return True, 0

        if self.check_rows_for_winner() or self.check_columns_for_winner() or self.check_diagonals_for_winner():
            return True, 1

        return False, None