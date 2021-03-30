# -*- coding: utf-8 -*-
import unittest
import game


class GameTest(unittest.TestCase):
    def test_is_part(self):
        test_game = game.Game()
        test_game.set_source_word("абрикос")
        self.assertTrue(test_game.is_part_of_source('коса'))
        self.assertTrue(test_game.is_part_of_source('бирка'))
        self.assertFalse(test_game.is_part_of_source('крик'))
        self.assertFalse(test_game.is_part_of_source('персик'))
        test_game.set_source_word("подушка")
        self.assertTrue(test_game.is_part_of_source('душа'))
        self.assertTrue(test_game.is_part_of_source('опушка'))
        self.assertFalse(test_game.is_part_of_source('кот'))
        self.assertFalse(test_game.is_part_of_source('персик'))

    def test_is_noun(self):
        self.assertTrue(game.is_noun("абрикос"))
        self.assertFalse(game.is_noun("абрикосовый"))

    def test_set_source(self):
        test_game = game.Game()
        test_game.set_source_word("абрикос")
        self.assertEqual(test_game.get_source_word(), 'абрикос')

    def test_choose_words(self):
        words = game.choose_source_words(10)
        self.assertEqual(len(words), 10)
        words = game.choose_source_words(5)
        self.assertEqual(len(words), 5)
        for word in words:
            self.assertIsInstance(word, str)

    def test_get_message(self):
        test_game = game.Game()
        test_game.set_source_word('контекст')
        self.assertEqual(test_game.get_message('кот'), "")
        self.assertEqual(test_game.get_message('Кот'), 'Это слово уже было')
        test_game.guessed_words.clear()
        self.assertEqual(test_game.get_message('Кот'), '')
        self.assertEqual(test_game.get_message('кот1'), 'Недопустимые символы')
        self.assertEqual(test_game.get_message('кость'), "В слове есть буквы не из исходного")
        self.assertEqual(test_game.get_message('некто'), "Нет такого существительного")


if __name__ == '__main__':
    unittest.main()
