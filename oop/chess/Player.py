from typing import Tuple, Dict

from oop.chess.Piece import Piece


class Player:
    chesses:Dict[str,Piece] = None

    # attribute name
    def __init__(self, name: str):
        self.name = name
        self.game = None

    def achive_chess(self, chesses: Dict[str,Piece]):
        self.chesses = chesses

    def move(self, name: str, position: Tuple):
        # is_active = self.game.move(piece, position)
        # return piece
        chess = self.chesses[name]
        status = chess.valid_move(position)
        if status:
            self.game.move(chess, position, self.name)

    def __str__(self):
        return self.name
