from oop.chess.Piece import Piece


class Rook(Piece):

    def __init__(self, x, y, name):
        super().__init__(x, y, name)

    def __str__(self):
        return super().__str__()

    def get_position(self):
        return super().get_position()

    def valid_move(self, new_pos: (), name: str):

        return super().valid_move(new_pos, name)