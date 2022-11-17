from typing import Tuple


class Piece:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.pos: Tuple[int,int] = (self.x, self.y)
        self.killed = False
        self.name = name

    def __str__(self):
        return f'{self.name}'

    def get_position(self):
        return self.pos

    def valid_move(self, new_pos: ()):
        return {
            "piece": self.name,
            "new_pos": new_pos
        }
