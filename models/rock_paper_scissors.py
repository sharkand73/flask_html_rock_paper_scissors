options = ["rock", "paper", "scissors"]
outcomes = ["It's a draw!", "Player 1 wins!", "Player 2 wins!"]

def process_outcome(name_1, name_2):
    rabbit = (options.index(name_1) - options.index(name_2)) % 3    # Pulls rabbit out
    return outcomes[rabbit]                                        # of maths hat.

