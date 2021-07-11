
from models.Player import Player
from models.Board import Board

class TicTacToe:

    def __init__(self):
        self.board = Board()
        self.player1 = Player('Player 1', 'X')
        self.player2 = Player('Player 2', 'O')
        self.current_player = None


    def new_game(self):
        self.board.reset_game_board()
        self.current_player = self.player1


    def get_current_player_position(self):
        return self.current_player.get_position_from_console()


    @staticmethod
    def show_game_instructions():
        print("\nEnter a value between 1-9: ")
        print("Positions of each number are as follows")
        print(" 1 | 2 | 3")
        print("-----------")
        print(" 4 | 5 | 6")
        print("-----------")
        print(" 7 | 8 | 9\n")


    def update_board(self, selected_position):
        player_piece = self.current_player.get_game_piece()
        self.board.update_board(selected_position, player_piece)

    def check_valid_position(self, position):
        return self.board.check_valid_position(position)

    def show_board(self):
        return self.board.show_board()


    def make_move(self):
        selected_position = self.get_current_player_position()
        while not self.check_valid_position(selected_position):
            print("Enter a Valid Position!")
            selected_position = self.get_current_player_position()

        self.update_board(selected_position)


    def switch_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1


    def check_game_over(self):
        is_game_over, result = self.board.check_game_over()
        if is_game_over:
            if result == 0:
                return True, "Its a Draw"
            else:
                return True, "{} wins the Game".format(self.current_player.name)
        return False, None


    def play_game(self):
        self.new_game()
        game_over = False
        game_result = None

        while not game_over:
            print("{}'s Turn".format(self.current_player.get_player_name()))
            self.show_game_instructions()
            self.make_move()
            self.show_board()
            game_over, game_result = self.check_game_over()
            self.switch_player()

        print(game_result)



game = TicTacToe()
game.play_game()