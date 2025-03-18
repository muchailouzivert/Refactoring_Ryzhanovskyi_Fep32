import unittest
from tennis_ref import TennisGameRefactored

class TestTennisGame(unittest.TestCase):

    def setUp(self):
        self.game = TennisGameRefactored("player1", "player2")

    def test_won_point(self):
        self.game.won_point("player1")
        self.assertEqual(self.game.p1points, 1)
        self.game.won_point("player2")
        self.assertEqual(self.game.p2points, 1)

    def test_print_score(self):
        self.game.won_point("player1")
        self.assertEqual(self.game.print_score(), "Fifteen-Love")
        self.game.won_point("player2")
        self.assertEqual(self.game.print_score(), "Fifteen-All")

    def test_is_equal(self):
        self.game.p1points = 2
        self.game.p2points = 2
        self.assertEqual(self.game.is_equal(), "Thirty-All")

    def test_different_scores(self):
        self.game.p1points = 3
        self.game.p2points = 1
        self.assertEqual(self.game.different_scores(), "Forty-Fifteen")

    def test_check_for_advantage(self):
        self.game.p1points = 4
        self.game.p2points = 3
        self.assertTrue(self.game.check_for_advantage())

    def test_advantage(self):
        self.game.p1points = 4
        self.game.p2points = 3
        self.assertEqual(self.game.advantage(), "Advantage player1")

    def test_check_for_winner(self):
        self.game.p1points = 4
        self.game.p2points = 0
        self.assertTrue(self.game.check_for_winner())

    def test_winner(self):
        self.game.p1points = 4
        self.game.p2points = 0
        self.assertEqual(self.game.winner(), "Win for player1")

    def test_check_for_tie(self):
        self.game.p1points = 2
        self.game.p2points = 2
        self.assertTrue(self.game.check_for_tie())

if __name__ == "__main__":
    unittest.main()

        