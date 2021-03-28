class Player:
    def __init__(self, name):
        self.name = name
        self.choice = None
        self.score = 0

    def assign_choice(self, choice):
        self.choice = choice

    def random_choice(self):
        from random import choice
        list = ["rock", "paper", "scissors"]
        self.choice = choice(list)


    