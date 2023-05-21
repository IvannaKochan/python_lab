from BoardGame import BoardGame

if __name__ == '__main__':
    first_game = BoardGame("Dixid", 3, 12, 12)
    print("current players after removing function: ", first_game.remove_player())

    print("current players after adding function: ", first_game.add_player())

    print("boolean answer for can_play function: ", first_game.can_play())
