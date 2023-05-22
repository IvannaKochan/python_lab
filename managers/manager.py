"""
Module: game_manager

This module defines the GameManager class for managing games.


Classes:
    GameManager:
        A class representing a game manager.

        Attributes:
            games (list): A list of game objects.

        Methods:
            add_game(game): Adds a game object to the list of games.
            find_games_younger_than(realise_year_the_oldest_game):
                    Finds games released after or in a given year.
            find_games_for_this_number_of_players(number_of_player):
                    Finds games suitable for a specific number of players.

"""


class GameManager:
    """
    A class representing a game manager.

    Attributes:
        games (list): A list of game objects.

    Methods:
        add_game(game): Adds a game object to the list of games.
        find_games_younger_than(realise_year_the_oldest_game):
            Finds games released after or in a given year.
        find_games_for_this_number_of_players(number_of_player):
            Finds games suitable for a specific number of players.
    """

    def __init__(self):
        """
        Initializes a GameManager object with an empty list of games.
        """
        self.games = []

    def add_game(self, game):
        """
        Adds a game object to the list of games.

        Args:
            game: An object of a class that is a descendant of the Game class.

        Returns:
            None
        """
        self.games.append(game)

    def find_games_younger_than(self, realise_year_the_oldest_game):
        """
        Finds and returns a list of games from the 'games' attribute that were released
            after or in the given year.

        Args:
            realise_year_the_oldest_game (int): The release year of the oldest game to consider.

        Returns:
            list: A list of game objects whose release year is greater than or equal
                to 'realise_year_the_oldest_game'.

        """
        return list(
            filter(
                lambda game: game.realise_year >= realise_year_the_oldest_game, self.games))

    def find_games_for_this_number_of_players(self, number_of_player):
        """
        Finds and returns a list of games from the 'games' attribute that are suitable
            for a specific number of players.

        Args:
            number_of_player (int): The number of players to consider.

        Returns:
            list: A list of game objects whose minimum and maximum number of
                    players includes 'number_of_player'.
        """
        return list(
            filter(
                lambda game: game.max_players >= number_of_player >= game.min_players, self.games))
