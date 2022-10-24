from oop.chess.Broad import Broad
from oop.chess.Piece import Piece
from oop.chess.Rook import Rook


class Player:
    def __init__(self, broad: Broad, rook_left, rook_right):
        self.broad = broad
        self.rook_left = rook_left
        self.rook_right = rook_right

    def move(self, piece: Piece):
        return piece
