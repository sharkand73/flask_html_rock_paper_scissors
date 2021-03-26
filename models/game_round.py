class GameRound:
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

    def winner(self):
        options = ["rock", "paper", "scissors"]
        winners = [None, self.player_1, self.player_2]
        rabbit = (options.index(self.player_1.choice) - options.index(self.player_2.choice)) % 3    # Pulls rabbit out
        return winners[rabbit]                                                                    # of maths hat.

