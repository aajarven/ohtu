import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_search_with_full_name_returns_matching_player(self):
        player = self.statistics.search("Kurri")
        self.assertEquals(player.name, "Kurri")

    def test_search_with_partial_name_returns_matching_player(self):
        player = self.statistics.search("men")
        self.assertEquals(player.name, "Semenko")

    def test_search_nonexistent_player(self):
        player = self.statistics.search("Mörkö")
        self.assertIsNone(player)

    def test_search_single_player_team(self):
        players = self.statistics.team("PIT")
        self.assertEquals(len(players), 1)
        
        player = players[0]
        self.assertEquals(player.name, "Lemieux")

    def test_search_bigger_team(self):
        players = self.statistics.team("EDM")
        self.assertEquals(len(players), 3)

    def test_top_scorers_returns_the_best_player(self):
        top_scorers = self.statistics.top_scorers(1)
        self.assertEquals(len(top_scorers), 1)
        self.assertEquals(top_scorers[0].name, "Gretzky")

    def test_top_scorers_returns_top_three(self):
        top_scorers = self.statistics.top_scorers(3)
        self.assertEquals(len(top_scorers), 3)
        self.assertEquals(top_scorers[2].name, "Yzerman")
