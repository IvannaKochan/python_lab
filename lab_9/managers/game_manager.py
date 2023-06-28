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

from lab_9.decorators.logger_decorator import method_call_history_decorator
from lab_9.decorators.lenght_decorator import length_decorator


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

    def __len__(self):
        """
        Returns the length of the games list.

        Returns:
            int: The length of the games list.
        """
        return len(self.games)

    def __getitem__(self, item):
        """
        Returns the item at the given index from the games list.

        Args:
            item: The index of the item to retrieve.

        Returns:
            Any: The item at the given index.
        """
        return self.games[item]

    def __iter__(self):
        """
        Returns an iterator object over the games list.

        Returns:
            Iterator: An iterator object over the games list.
        """
        return iter(self.games)

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

        return list(filter(lambda game: game.realise_year >= realise_year_the_oldest_game, self.games))

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
        return list(filter(lambda game: game.max_players >= number_of_player >= game.min_players, self.games))

    def list_of_can_play(self):
        """
        Returns a list of boolean values indicating whether each game can be played.

        Returns:
            list: A list of boolean values indicating whether each game can be played.
        """
        return [game.can_play() for game in self.games]

    def enumerate_list(self):
        """
        Returns a list of formatted strings containing the game and its index.

        Returns:
            list: A list of formatted strings containing the game and its index.
        """
        return [f"{game} {index}" for index, game in enumerate(self.games)]

    @method_call_history_decorator("lab_9\history_method.txt")
    # @length_decorator
    def zip_list(self):
        """
        Returns a list of formatted strings combining each game with its can_play() value.

        Returns:
            list: A list of formatted strings combining each game with its can_play() value.
        """
        return [f"{game}{method}" for game, method in zip(self.games, self.list_of_can_play())]

    def dict_type(self, data_type):
        return [game.get_attributes_by_type(data_type) for game in self.games]

    def dict_condition_can_play(self):
        """
        :return: dict of any() and all() result
        """
        return {"any": any(self.list_of_can_play()), "all": all(self.list_of_can_play())}
