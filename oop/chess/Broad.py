from typing import Dict, Tuple, List

from oop.chess.Cell import Cell
from oop.chess.Piece import Piece
from oop.chess.Rook import Rook


class Broad:
    class Rule:
        position = {
            'black': {
                'rook_left': Rook(0, 0, 'rock_black_left'),
                'rook_right': Rook(7, 0, 'rock_black_right'),
            },
            'white': {
                'rook_left': Rook(0, 7, 'rock_white_left'),
                'rook_right': Rook(7, 7, 'rock_white_right'),
            },
        }

    def __init__(self, n: int = 8):
        self.n = n
        self.matrix: List[List[Cell]] = [[Cell() for i in range(self.n)] for j in range(self.n)]
        self.start_game = {}
        # self.draw()

    def draw(self):
        size = self.n * self.n
        # black = 0
        white = 1
        for vertical in range(len(self.matrix)):
            for horizontal in range(len(self.matrix)):
                if (vertical + horizontal) % 2 == 0:
                    self.matrix[vertical][horizontal] = white
        return self.matrix

    def print(self):
        for row in self.matrix:
            for cell in row:
                print(cell, end="\t")
            print()

    def move(self, color_player: str, chess: Piece, position: Tuple) -> bool:
        # SAU NAY XONG VALIDATE MOVE THI XET THEM PLAYER COLOR
        if self.valide_move(chess, position):
            old_pos = chess.pos
            self.matrix[old_pos[0]][old_pos[1]].name_piece = None
            self.matrix[position[0]][position[1]].name_piece = chess.name
            chess.x = position[0]
            chess.y = position[1]
            chess.pos = (chess.x,chess.y)



        else:
            return False

    def valide_move(self,chess:Piece ,position: Tuple) -> bool:
        return True

    def build(self) -> Dict:
        broad_position = self.Rule.position
        for player in broad_position:
            player = broad_position[player]
            for name_chess in player:
                chess: Piece = player[name_chess]
                poss = chess.pos
                self.matrix[poss[1]][poss[0]].name_piece = chess
        print(self.print())
        return broad_position
