import unittest
import pygame
from pygame.locals import KEYDOWN, K_RETURN
from unittest.mock import patch
from CSF_02230300_CAP2 import JumbleWordGame 
import sys

class CustomTestResult(unittest.TextTestResult):
    def addSuccess(self, test):
        super().addSuccess(test)
        print(f"Pass: {test}")

    def addFailure(self, test, err):
        super().addFailure(test, err)
        print(f"Fail: {test}")

class JumbleWordGameTests(unittest.TestCase):
    def test_jumble_word(self):
        word = "apple"
        jumbled_word = self.game.jumble_word(word)
        self.assertNotEqual(word, jumbled_word)

    def test_unjumble_word(self):
        jumbled_word = "papel"
        unjumbled_word = self.game.unjumble_word(jumbled_word)
        self.assertEqual(unjumbled_word, "apple")

    def test_increment_score(self):
        self.game.increment_score(10)
        self.assertEqual(self.game.score, 10)

    def test_level_up(self):
        self.game.level_up()
        self.assertEqual(self.game.current_level_index, 1)

    def test_is_game_over_false(self):
        self.assertFalse(self.game.is_game_over())

    def test_is_game_over_true(self):
        self.game.lives = 0
        self.assertTrue(self.game.is_game_over())

    def test_get_current_level(self):
        expected_level = {
            "level_index": 0,
            "word_bank": ["apple", "banana", "cherry"],
            "time_limit": 60
        }
        current_level = self.game.get_current_level()
        self.assertDictEqual(current_level, expected_level)

    def test_is_time_up_false(self):
        self.assertFalse(self.game.is_time_up())

    def test_is_time_up_true(self):
        self.game.time_left = -1
        self.assertTrue(self.game.is_time_up())

    def test_decrement_time(self):
        initial_time_left = self.game.time_left
        self.game.decrement_time(5)
        self.assertEqual(self.game.time_left, initial_time_left - 5)
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(JumbleWordGameTests)
    result = CustomTestResult(stream=sys.stdout, descriptions=True, verbosity=2)
    runner = unittest.TextTestRunner(resultclass=CustomTestResult)
    runner.run(suite)
