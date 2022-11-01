from typing import Tuple, Dict

from oop.chess.Piece import Piece


class Player:
    chesses = None

    # attribute name
    def __init__(self, name: str):
        self.name = name
        self.game = None

    def join_game(self, game):
        self.game = game

    def achive_chess(self, chesses: Dict):
        self.chesses = chesses

    def move(self, name: str, position: Tuple):
        # is_active = self.game.move(piece, position)
        # return piece
        status = self.chesses[name].valid_move(position)
        if status :
            self.game.move(name,position)
    def __str__(self):
        return self.name
