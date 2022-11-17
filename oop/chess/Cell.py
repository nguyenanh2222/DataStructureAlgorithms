class Cell():

    def __init__(self, name_piece=None):
        self.name_piece: str = name_piece
        self.position = {
            "x": range(7),
            "y": range(7)
        }


    def __str__(self):
        return f"{self.name_piece}"
