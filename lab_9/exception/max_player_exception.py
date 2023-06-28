class MaxPlayersException(Exception):
    message = "Not normal number of players"

    def __init__(self):
        super().__init__(MaxPlayersException.message)

