class Cell():


          def __init__(self, name_piece=None):
            self.name_piece: str = name_piece
            self.position = {
            "x": range(7),
            "y": range(7)
          }





    def __str__(self):
        return f"piece: {self.name_piece}, position {self.position}"


c = Cell()
c.position = {
    "x": 8,
    "y": 8
}
print(c.position)
