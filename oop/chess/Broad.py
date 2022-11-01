from typing import Dict, Tuple

from oop.chess.Rook import Rook


class Broad:
    class Rule:
        position = {
            'black': {
                'rook_left': Rook(0, 0, 'rock_black_left'),
                'rook_right': Rook(0, 7, 'rock_black_white'),
            },
            'white': {
                'rook_left': Rook(7, 0, 'rock_white_left'),
                'rook_right': Rook(7, 7, 'rock_white_right'),
            },
        }

        def get_chess(self):
            return self.position

    def __init__(self, n: int):
        self.n = n
        self.broad = [[0 for i in range(self.n)] for j in range(self.n)]
        self.start_game = {}
        self.draw()

    def draw(self):
        size = self.n * self.n
        # black = 0
        white = 1
        for vertical in range(len(self.broad)):
            for horizontal in range(len(self.broad)):
                if (vertical + horizontal) % 2 == 0:
                    self.broad[vertical][horizontal] = white
        return self.broad

    def print(self):
        for i in self.broad:
            for j in i:
                print(j, end="\t")
            print()

    def move(self, name: str, position: Tuple):
        ...

    def valide_move(self, position: Tuple):
        ...

    def build(self) -> Dict:
        chesses = self.Rule().get_chess()
        for chess in chesses:
            chess = chesses[chess]
            for chess_position in chess:
                data = chess[chess_position].get_position()
                self.broad[data[1]][data[0]] = chess[chess_position]
        print(self.print())
        return chesses
