class BoardGame:

    def __init__(self, title, min_players, max_players, current_players):
        self.title = title
        self.min_players = min_players
        self.max_players = max_players
        self.current_players = current_players

    def remove_player(self):
        return self.current_players - 1

    def add_player(self):
        return self.current_players + 1 if self.current_players < self.max_players else self.current_players

    def can_play(self):
        return self.current_players >= self.min_players and self.current_players <= self.max_players
