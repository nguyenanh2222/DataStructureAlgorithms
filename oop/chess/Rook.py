from oop.chess.Piece import Piece


class Rook(Piece):

    def __init__(self, x, y, name):
        super().__init__(x, y, name)

    def __str__(self):
        return super().__str__()

    def get_position(self):
        return super().get_position()

    def vertical(self, y: int)-> tuple:
        return (self.x, y)

    def hozical(self, x: int)-> tuple:
        return (x, self.y)
    def valid_move(self, new_pos: ()) -> bool:
        old_pos = self.pos
        if new_pos[0] > 8 or new_pos[1] > 8:
            return False
        elif new_pos == old_pos:
            return False
        elif new_pos == self.vertical(new_pos[1]) or new_pos == self.hozical(new_pos[0]):
            return True
        else:
            return False


