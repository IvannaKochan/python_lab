"""
A class representing a board game, inheriting from the Game class.
"""
from lab_9.models.game import Game


class BoardGame(Game):
    """
    A class representing a board game, inheriting from the Game class.

    Attributes:
        title (str): The title of the board game.
        publisher (str): The publisher of the board game.
        realise_year (int): The year the board game was released.
        min_players (int): The minimum number of players required to play the board game.
        max_players (int): The maximum number of players allowed to play the board game.
        current_players (int): The current number of players in the board game.

    Methods:
        disconnect_player(): Overrides the parent class method to disconnect a player
                    from the board game.
        connect_player(): Overrides the parent class method to connect a player to the board game.
        can_play(): Overrides the parent class method to check if the board game can be played.
        to_string(): Overrides the parent class method to convert the object's attributes
                    to a string representation.

    """

    def __init__(self, title: str = "", publisher: str = "", realise_year: int = 0, min_players: int = 0,
                 max_players: int = 0, current_players: int = 0):
        """
        Initializes a BoardGame object.

        Args:
            title (str): The title of the board game.
                        Defaults to an empty string.
            publisher (str): The publisher of the board game.
                        Defaults to an empty string.
            realise_year (int): The year the board game was released.
                        Defaults to 0.
            min_players (int): The minimum number of players required to play
                        the board game. Defaults to 0.
            max_players (int): The maximum number of players allowed to play
                        the board game. Defaults to 0.
            current_players (int): The current number of players in the board
                        game. Defaults to 0.

        """
        super().__init__(publisher, realise_year, current_players)
        self.title = title
        self.min_players = min_players
        self.max_players = max_players
        self.set_of_language = {"ukrainian", "chinese"}

    def disconnect_player(self):
        """
        Overrides the parent class method to disconnect a player from the board game.

        Returns:
            int: The number of players after disconnecting one player.

        """
        return self.current_players - 1

    def connect_player(self):
        """
        Overrides the parent class method to connect a player to the board game.

        Returns:
            int: The current number of players after adding a player, unless the maximum limit
            is reached, then the current number of players remains unchanged.

        """
        return self.current_players + 1 if self.current_players < self.max_players else self.current_players

    def can_play(self):
        """
        Overrides the parent class method to check if the board game can be played.

        Returns:
            bool: True if the current number of players is within the specified range,
                  False otherwise.

        """
        return self.max_players >= self.current_players >= self.min_players

    def __str__(self):
        """
        Overrides the parent class method to convert the object's attributes
            to a string representation.

        Returns:
            str: A string representation of the BoardGame object.

        """
        return f"Board Game: {self.title}, {self.publisher}, {self.realise_year}, {self.min_players}, " \
               f"{self.max_players}, {self.current_players}"
