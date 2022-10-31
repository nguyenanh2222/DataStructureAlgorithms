class Piece:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.pos = (self.x, self.y)
        self.killed = False
        self.name = name

    def __str__(self):
        return f'{self.name} is stay in {self.pos}'

    def get_position(self):
        return self.pos

    def valid_move(self, new_pos: (), name: str):
        return {
            "piece": name,
            "new_pos": new_pos
        }
