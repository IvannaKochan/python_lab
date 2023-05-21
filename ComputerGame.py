from Game import Game


class ComputerGame(Game):
    __title = None
    __min_players = None
    __max_players = None

    def __init__(self, title="", publisher="", relise_year=0, min_players=0, max_players=0, current_players=0):
        super().__init__(publisher, relise_year, current_players)
        self.__title = title
        self.__min_players = min_players
        self.__max_players = max_players

    def disconnect_player(self):
        return self.current_players - 1

    def connect_player(self):
        return self.current_player + 1 if self.current_players < self.max_players else self.current_players

    def can_play(self):
        return self.max_players >= self.current_players >= self.min_players
