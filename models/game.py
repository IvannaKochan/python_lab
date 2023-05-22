from abc import ABC, abstractmethod


class Game(ABC):

    def __init__(self, publisher="", relise_year=0, current_players=0):
        self.publisher = publisher
        self.relise_year = relise_year
        self.current_players = current_players

    @abstractmethod
    def disconnect_player(self):
        """
        disconnect one player from the game;
        :arg current_players - integer

        :return: number of player - 1
        """

    @abstractmethod
    def connect_player(self):
        """
        connect one player if current number of players is less than max
        :arg current_players and max_players - integer

        :return: integer current_payer after adding a person
        """

    @abstractmethod
    def can_play(self):
        """
        :arg current_player, min_players and max_players - integer

        :return: boolean true if current_players is less or equal to max_players and more or equal to min_players
                         false in the other situations
        """

    @abstractmethod
    def to_string(self):
        """
        Method convert all atrebuts to string and return it

        :return: a string representation of an object
        """