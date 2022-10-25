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
        print(self.name, self.chesses)

    def move(self, piece: Piece, position: Tuple):
        is_active = self.game.move(piece, position)
        return piece

    def __str__(self):
        return self.name
