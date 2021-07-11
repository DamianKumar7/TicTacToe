

class Player:

    def __init__(self, game_piece: str):
        self.game_piece = game_piece


    def get_game_piece(self):
        return self.game_piece

    @staticmethod
    def take_position_as_input_from_console() -> str:
        print("Enter Position to place the piece: ", end="")
        piece_position = input()
        return piece_position

