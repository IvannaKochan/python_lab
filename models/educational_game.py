"""
A class representing an educational game, inheriting from the Game class.
"""

from lab_8.models.game import Game


class EducationalGame(Game):
    """
    A class representing an educational game, inheriting from the Game class.

    Attributes:
        title (str): The title of the educational game.
        publisher (str): The publisher of the educational game.
        realise_year (int): The year the educational game was released.
        min_players (int): The minimum number of players required to play the educational game.
        max_players (int): The maximum number of players allowed to play the educational game.
        current_players (int): The current number of players in the educational game.

    Methods:
        disconnect_player(): Overrides the parent class method to disconnect a player
                    from the educational game.
        connect_player(): Overrides the parent class method to connect a player
                    to the educational game.
        can_play(): Overrides the parent class method to check if the educational game
                    can be played.
        to_string(): Overrides the parent class method to convert the object's attributes
                    to a string representation.

    """

    def __init__(self, title="", publisher="", realise_year=0, min_players=0, max_players=0,
                 current_players=0):
        """
        Initializes an EducationalGame object.

        Args:
            title (str): The title of the educational game.
                        Defaults to an empty string.
            publisher (str): The publisher of the educational game.
                        Defaults to an empty string.
            realise_year (int): The year the educational game was released.
                        Defaults to 0.
            min_players (int): The minimum number of players required to play
                        the educational game. Defaults to 0.
            max_players (int): The maximum number of players allowed to play
                        the educational game. Defaults to 0.
            current_players (int): The current number of players in
                        the educational game. Defaults to 0.

        """
        super().__init__(publisher, realise_year, current_players)
        self.title = title
        self.min_players = min_players
        self.max_players = max_players

    def disconnect_player(self):
        """
        Overrides the parent class method to disconnect a player from the educational game.

        Returns:
            int: The number of players after disconnecting one player.

        """
        return self.current_players - 1

    def connect_player(self):
        """
        Overrides the parent class method to connect a player to the educational game.

        Returns:
            int: The current number of players after adding a player, unless the maximum limit
                    is reached, then the current number of players remains unchanged.

        """
        return (self.current_players + 1) if self.current_players < self.max_players else self.current_players

    def can_play(self):
        """
        Overrides the parent class method to check if the educational game can be played.

        Returns:
            bool: True if the current number of players is within the specified range,
                  False otherwise.

        """
        return self.max_players >= self.current_players >= self.min_players

    def to_string(self):
        """
        Overrides the parent class method to convert the object's attributes
            to a string representation.

        Returns:
            str: A string representation of the EducationalGame object.

        """
        return "Educational Game" + self.title + ", publisher " + self.publisher \
            + ", realise year " + str(self.realise_year) + ", min players " \
            + str(self.min_players) + ", max players " + str(self.max_players) \
            + ", current player " + str(self.current_players)
