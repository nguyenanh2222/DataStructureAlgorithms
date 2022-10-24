from oop.chess.Player import Player
from oop.chess.Rook import Rook


class Broad:
    class Rule:
        position = {
            'player1': {
                'rook_left': Rook(0, 0),
                'rook_right': Rook(0, 7),
                # chi di thang, di nang trong ban co, khong di len quan minh

            }
        }
        # player1 = position['player1']
        # for name_chess in player1:
        #     chess_position = player1[name_chess]
        #     for index in range(len(chess_position)):
        #         print(f'{name_chess}_{index}')

    def __init__(self, n: int):
        self.n = n
        self.broad = [[0 for i in range(self.n)] for j in range(self.n)]
        self.start_game = {}

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
            print(i)

    def build(self):
        player1 = Player(self, rook_left=Rook(0, 0), rook_right=Rook(0, 7))
        player2 = Player(self, rook_left=Rook(7, 0), rook_right=Rook(7, 7))

        self.start_game = {
            'player1':
                {
                    'rook_left': player1.rook_left,
                    'rook_right': player1.rook_right
                },
            'player2':
                {
                    'rook_left': player2.rook_left,
                    'rook_right': player2.rook_right
                }
        }


chess = Broad(8)
chess.draw()
chess.print()
