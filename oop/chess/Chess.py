from typing import Tuple

from oop.chess.Broad import Broad
from oop.chess.Piece import Piece
from oop.chess.Player import Player

BLACK = 'black'
WHITE = 'white'
class ChessGame:
    chess = Broad(8)

    player = {
        BLACK: None,
        WHITE: None
    }

    def __init__(self):
        pass

    def join_game(self, player1: Player, player2: Player):
        self.player[BLACK] = player1
        self.player[WHITE] = player2
        chesses = self.chess.build()
        self.player[BLACK].achive_chess(chesses[BLACK])
        self.player[WHITE].achive_chess(chesses[WHITE])

    def move(self, name: str, position: Tuple):
        self.chess.move(name, position)


    def show_borad(self):
        print(self.chess)