from lab_8.managers.manager import GameManager
from lab_8.models.educational_game import EducationalGame
from lab_8.models.mobile_game import MobileGame
from models.board_game import BoardGame
from models.computer_game import ComputerGame

game_list = GameManager()

for _ in range(2):
    game_list.add_game(BoardGame("Dixid", "First Company", 2018, 3, 12, 12))
    game_list.add_game(ComputerGame("S.T.A.L.K.E.R. 2", "GSC Game World", 2023, 2, 100, 1))
    game_list.add_game(MobileGame("Clash Of Clans","Publisher 2", 2012, 2, 2, 2))
    game_list.add_game(EducationalGame("AR Book", "Publisher 3", 2023, 1, 1, 1))

for game in game_list.games:
    print(game)

print("\n")

list_games_yanger_than = game_list.find_games_younger_than(2021)
for _ in list_games_yanger_than:
    print(_)

print("\n")

list_games_for_needed_player = game_list.find_games_for_this_number_of_players(10)
for _ in list_games_for_needed_player:
    print(_)
