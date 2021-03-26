import unittest
from models.player import Player
from models.game_round import GameRound

class TestGameRound(unittest.TestCase):
    def setUp(self):
        self.player_1 = Player("Andy")
        self.player_2 = Player("Evelyn")
        self.player_1.assign_choice("rock")
        self.player_2.assign_choice("paper")
        self.current_round = GameRound(self.player_1, self.player_2)

    #@unittest.skip("")
    def test_players_in_round(self):
        self.assertEqual("Andy", self.current_round.player_1.name)
        self.assertEqual("Evelyn", self.current_round.player_2.name)

    #@unittest.skip("")
    def test_player_choices_in_round(self):
        self.assertEqual("rock", self.current_round.player_1.choice)
        self.assertEqual("paper", self.current_round.player_2.choice)

    #@unittest.skip("")
    def test_winner_rock_paper(self):
        self.assertEqual("Evelyn", self.current_round.winner().name)

    #@unittest.skip("")
    def test_winner_paper_rock(self):
        self.player_1.assign_choice("paper")
        self.player_2.assign_choice("rock")        
        self.assertEqual("Andy", self.current_round.winner().name)

    #@unittest.skip("")
    def test_winner_scissors_paper(self):
        self.player_1.assign_choice("scissors")
        self.player_2.assign_choice("paper")
        self.assertEqual("Andy", self.current_round.winner().name)

    #@unittest.skip("")
    def test_winner_paper_scissors(self):
        self.player_1.assign_choice("paper")
        self.player_2.assign_choice("scissors")
        self.assertEqual("Evelyn", self.current_round.winner().name)

    #@unittest.skip("")
    def test_winner_rock_scissors(self):
        self.player_1.assign_choice("rock")
        self.player_2.assign_choice("scissors")
        self.assertEqual("Andy", self.current_round.winner().name)

    #@unittest.skip("")
    def test_winner_scissors_rock(self):
        self.player_1.assign_choice("scissors")
        self.player_2.assign_choice("rock")
        self.assertEqual("Evelyn", self.current_round.winner().name)

    #@unittest.skip("")
    def test_winner_rock_rock(self):
        self.player_1.assign_choice("rock")
        self.player_2.assign_choice("rock")
        self.assertIsNone(self.current_round.winner())

    @unittest.skip("")
    def test_winner_scissors_scissors(self):
        self.player_1.assign_choice("scissors")
        self.player_2.assign_choice("scissors")
        self.assertIsNone(self.current_round.winner())

    @unittest.skip("")
    def test_winner_paper_paper(self):
        self.player_1.assign_choice("paper")
        self.player_2.assign_choice("paper")
        self.assertIsNone(self.current_round.winner())

    

    
