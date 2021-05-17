import unittest
from game import TicTacToe

import HtmlTestRunner
import xmlrunner


class TestWinner(unittest.TestCase):
    def setUp(self):
        self.test_game = TicTacToe()

    def test_winner_row(self):
        self.test_game.board = ['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ']
        self.test_game.print_board()
        self.assertTrue(self.test_game.winner(2, 'X'))
        self.test_game.board = [' ', ' ', ' ', 'X', 'X', 'X', ' ', ' ', ' ']
        self.test_game.print_board()
        self.assertTrue(self.test_game.winner(5, 'X'))
        self.test_game.board = [' ', ' ', ' ', ' ', ' ', ' ', 'X', 'X', 'X']
        self.test_game.print_board()
        self.assertTrue(self.test_game.winner(8, 'X'))

    def test_winner_colum(self):
        self.test_game.board = ['X', ' ', ' ', 'X', ' ', ' ', 'X', ' ', ' ']
        self.test_game.print_board()
        self.assertTrue(self.test_game.winner(0, 'X'))
        self.test_game.board = [' ', 'X', ' ', ' ', 'X', ' ', ' ', 'X', ' ']
        self.test_game.print_board()
        self.assertTrue(self.test_game.winner(1, 'X'))
        self.test_game.board = [' ', ' ', 'X', ' ', ' ', 'X', ' ', ' ', 'X']
        self.test_game.print_board()
        self.assertTrue(self.test_game.winner(2, 'X'))

    def test_winner_diagonal_1(self):
        self.test_game.board = ['X', ' ', ' ', ' ', 'X', ' ', ' ', ' ', 'X']
        self.test_game.print_board()
        self.assertTrue(self.test_game.winner(0, 'X'))

    def test_winner_diagonal_2(self):
        self.test_game.board = [' ', ' ', 'X', ' ', 'X', ' ', 'X', ' ', ' ']
        self.test_game.print_board()
        self.assertTrue(self.test_game.winner(2, 'X'))

    def test_winner_lose(self):
        self.test_game.board = ['X', 'O', 'X', ' ', ' ', ' ', 'X', ' ', ' ']
        self.test_game.print_board()
        self.assertFalse(self.test_game.winner(0, 'X'))
        self.test_game.board = [' ', ' ', 'X', 'O', 'X', ' ', ' ', ' ', ' ']
        self.test_game.print_board()
        self.assertFalse(self.test_game.winner(2, 'X'))
        self.test_game.board = [' ', ' ', 'O', ' ', 'X', ' ', ' ', ' ', ' ']
        self.test_game.print_board()
        self.assertFalse(self.test_game.winner(5, 'X'))


def run_tests():
    unittest.main()


def html_report():
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reportHTML'))



def xml_report():
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='./reportXML'))


if __name__ == '__main__':
    run_tests()
