"""
Main method
"""
# from lab_9.managers.set_manager import SetManager
from lab_9.managers.game_manager import GameManager
from lab_9.models.educational_game import EducationalGame
from lab_9.models.mobile_game import MobileGame
from lab_9.models.board_game import BoardGame
from lab_9.models.computer_game import ComputerGame

game_list = GameManager()

for _ in range(2):
    game_list.add_game(BoardGame(" Dixid", "First Company", 2018, 3, 12, 13))
    game_list.add_game(ComputerGame(" S.T.A.L.K.E.R. 2", "GSC Game World", "Windows", 2023, 2, 100, 1))
    game_list.add_game(MobileGame(" Clash Of Clans", "Publisher 2", 1.3, 2012, 1, 2, 2))
    game_list.add_game(EducationalGame(" AR Book", "Publisher 3", "Physics", 2023, 1, 1, 1))

for game in game_list.games:
    print(game.__str__())

# realise_year = 2021
# number_of_players = 10
#
# print("\nList of game younger than ", realise_year)
#
# list_games_younger_than = game_list.find_games_younger_than(realise_year)
# for element in list_games_younger_than:
#     print(element.title, element.realise_year)
#
# print("\nList of game for ", number_of_players, " players")
#
# list_games_for_needed_player = game_list.find_games_for_this_number_of_players(number_of_players)
# for element in list_games_for_needed_player:
#     print(element.title, "min players ", element.min_players, "max players ", element.max_players)

# a = game_list.list_of_can_play()
# print(a)
# print("\n")
# b = game_list.enumerate_list()
# print(b)
# print("\n")
# c = game_list.zip_list()
# print(c)

# d = game_list.dict_condition_can_play()
# print(d)

# print("\n")
# f = game_list.dict_type(int)
# for _ in f:
#     print(_)
# print(game_list[0].can_play())

for game in game_list.games:
    print(game.can_play())
