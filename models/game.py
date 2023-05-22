"""
Module: game

This module defines the abstract base class Game and its subclasses
    representing different types of games.
"""

from abc import ABC, abstractmethod


class Game(ABC):
    """
        Abstract base class representing a game.

        Attributes:
            publisher (str): The publisher of the game.
            realise_year (int): The year the game was released.
            current_players (int): The current number of players in the game.

        Methods:
            disconnect_player(): Abstract method to disconnect a player from the game.
            connect_player(): Abstract method to connect a player to the game.
            can_play(): Abstract method to check if the game can be played.
            to_string(): Abstract method to convert the object's attributes
                to a string representation.

        """

    def __init__(self, publisher="", realise_year=0, current_players=0):
        """
                Initializes a Game object.

                Args:
                    publisher (str): The publisher of the game. Defaults to an empty string.
                    realise_year (int): The year the game was released. Defaults to 0.
                    current_players (int): The current number of players in the game. Defaults to 0.

                """
        self.publisher = publisher
        self.realise_year = realise_year
        self.current_players = current_players

    @abstractmethod
    def disconnect_player(self):
        """
        Abstract method to disconnect a player from the game.

        Returns:
            int: The number of players after disconnecting one player.

        """

    @abstractmethod
    def connect_player(self):
        """
        Abstract method to connect a player to the game.

        Returns:
            int: The current number of players after adding a player.

        """

    @abstractmethod
    def can_play(self):
        """
        Abstract method to check if the game can be played.

        Returns:
            bool: True if the current number of players is within the specified range,
                  False otherwise.

        """

    @abstractmethod
    def to_string(self):
        """
        Abstract method to convert the object's attributes to a string representation.

        Returns:
            str: A string representation of the object.

        """
