class GameRound:
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

    def winner(self):
        options = ["rock", "paper", "scissors"]
        winners = [None, self.player_1, self.player_2]
        rabbit = (options.index(self.player_1.choice) - options.index(self.player_2.choice)) % 3    # Pulls rabbit
        return winners[rabbit]                                                                    # out of maths hat.
        
    def loser(self):
        players = [self.player_1, self.player_2]
        index = players.index(self.winner())
        return players[(not index)]                                                                 

    def update_score(self):
        if self.winner():
            self.winner().score += 1

    def champion(self):
        if self.player_1.score > self.player_2.score:
            return self.player_1
        elif self.player_2.score > self.player_1.score:
            return self.player_2
        else: return None

