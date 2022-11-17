from typing import Tuple

from oop.chess.Broad import Broad
from oop.chess.Player import Player

BLACK = 'black'
WHITE = 'white'


class ChessGame:
    broad = Broad(8)

    player = {
    }

    def __init__(self):
        pass

    def join_game(self, player1: Player, player2: Player):
        self.player[player1.name] = BLACK
        self.player[player2.name] = WHITE
        player1.game = self
        player2.game = self
        chesses_position = self.broad.build()
        player1.achive_chess(chesses_position[BLACK])
        player2.achive_chess(chesses_position[WHITE])

    def move(self, chess, position: Tuple, player: str):
        color_player = self.player[player]
        self.broad.move(color_player, chess, position)
        self.show_borad()
    def show_borad(self):
        self.broad.print()
