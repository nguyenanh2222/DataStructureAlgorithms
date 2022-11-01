from oop.chess.ChessGame import ChessGame
from oop.chess.Player import Player

game = ChessGame()

player1 = Player(name="black")
player2 = Player(name="while")
game.join_game(player1, player2)

player1.move("rook_left", (0, 2))
player1.move("rook_left", (0, 6))
