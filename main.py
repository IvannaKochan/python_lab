from BoardGame import BoardGame
from ComputerGame import ComputerGame

if __name__ == '__main__':
    board_game = BoardGame("Dixid", "First Company", 2018, 3, 12, 12)

    print("current players after disconnecting function: ", board_game.disconnect_player())

    print("current players after connecting function: ", board_game.connect_player())

    print("boolean answer for can_play function: ", board_game.can_play())

    computer_game = ComputerGame("S.T.A.L.K.E.R. 2", "GSC Game World", 2023, 2, 100, 1)

    print("current players after disconnecting function: ", computer_game.disconnect_player())

    print("current players after connecting function: ", computer_game.connect_player())

    print("boolean answer for can_play function: ", computer_game.can_play())

    game_list = []
    game_list.append(board_game)
    game_list.append(computer_game)

