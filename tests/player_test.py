import unittest
from models.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player_1 = Player("Andy")

    def test_player_has_name(self):
        self.assertEqual("Andy", self.player_1.name)

    def test_player_choice(self):
        self.player_1.assign_choice("rock")
        self.assertEqual("rock", self.player_1.choice)

