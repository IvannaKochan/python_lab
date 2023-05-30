from lab_9.managers.game_manager import GameManager


class SetManager:
    def __init__(self, game_manager: GameManager = GameManager()):
        self.game_manager = game_manager


def __iter__(self):
    for game in self.game_manager:
        for language in game.set_of_language:
            yield language


def __len__(self):
    count = 0
    for game in self.game_manager:
        count += len(game.set_of_language)
    return count


def __next__(self):
    for game in self.game_manager:
        for language in game.set_of_language:
            yield language


def __getitem__(self, index):
    for game in self.game_manager:
        language_set = game.set_of_language
        if index < len(language_set):
            return list(language_set)[index]
        index -= len(language_set)
    raise IndexError("Index out of range")
