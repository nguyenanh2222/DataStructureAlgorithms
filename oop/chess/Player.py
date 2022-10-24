from oop.chess.Piece import Piece
from oop.chess.Rook import Rook


class Player:
    def __init__(self, rook_left: Rook, rook_right: Rook):
        # self.broad = broad
        self.rook_left = rook_left
        self.rook_right = rook_right

    def move(self, piece: Piece):
        return piece
