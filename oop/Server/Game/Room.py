from oop.Server.Game.User import User


class Room:
    players = {
        'player1': None,
        'player2': None
    }

    def join_room(self, player: User) -> bool:
        for pos in self.players:
            if self.players[pos] is not None:
                self.players[pos] = player
        return False
