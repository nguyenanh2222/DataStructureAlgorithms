from oop.chess.Chess import ChessGame
from oop.chess.Player import Player

game = ChessGame()

player1 = Player(name="Sang")
player2 = Player(name="Anh")
game.join_game(player1, player2)

