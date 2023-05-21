from abc import ABC, abstractmethod


class Game(ABC):
    __publisher = None
    __relise_year = None
    __current_players = None

    def __init__(self, publisher="", relise_year=0, current_players=0):
        self.__publisher = publisher
        self.__relise_year = relise_year
        self.__current_players = current_players

    @abstractmethod
    def disconnect_player(self):
        """
        disconnect one player from the game;
        :arg __current_players - integer

        :return: number of player - 1
        """

    @abstractmethod
    def connect_player(self):
        """
        connect one player if current number of players is less than max
        :arg __current_players and __max_players - integer

        :return: integer __current_payer after adding a person
        """

    @abstractmethod
    def can_play(self):
        """
        :arg __current_player, __min_players and __max_players - integer

        :return: boolean true if __current_players is less or equal to __max_players and more or equal to __min_players
                         false in the other situations
        """
