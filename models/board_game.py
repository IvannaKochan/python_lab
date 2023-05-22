from lab_8.models.game import Game


class BoardGame(Game):

    def __init__(self, title="", publisher="", relise_year=0, min_players=0, max_players=0, current_players=0):
        super().__init__(publisher, relise_year, current_players)
        self.title = title
        self.min_players = min_players
        self.max_players = max_players

    def disconnect_player(self):
        return self.current_players - 1

    def connect_player(self):
        return self.current_players + 1 if self.current_players < self.max_players else self.current_players

    def can_play(self):
        return self.max_players >= self.current_players >= self.min_players

    def to_string(self):
        return "Board Game" + self.title + ", publisher " + self.publisher + ", relise year " + self.relise_year + \
            ", min players " + self.min_players + ", max players " + self.max_players + ", current player " \
            + self.current_players