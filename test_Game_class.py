import builtins
import unittest
from unittest.mock import patch
from unittest import mock
from Game_class import Game
from Player_class import Player
from TreasureMap_class import TreasureMap


class TestGame(unittest.TestCase):
    # @patch('builtins.input', lambda *args: [1,'5,h'])

    def test_game_start_limit(self):
        new_map = TreasureMap()
        new_player = Player(12)
        my_game = Game(new_player, new_map)
        my_game.player.attempt = 11
        my_game.player.limit = 12
        my_game.treasure_map.x = 5
        my_game.treasure_map.y = 'F'
        inputs = iter([1, '5,h'])
        mock.builtins.input = lambda _: next(inputs)
        self.assertEqual(my_game.game_start(), 'Количество попыток исчерпано. Сокровище не найдено.')

    def test_game_start_limit_win(self):
        new_map = TreasureMap()
        new_player = Player(3)
        my_game = Game(new_player, new_map)
        my_game.player.attempt = 0
        my_game.player.limit = 3
        my_game.treasure_map.x = 5
        my_game.treasure_map.y = 'F'
        inputs = iter([1, '5,h', 1, '5,f'])
        mock.builtins.input = lambda _: next(inputs)
        self.assertEqual(my_game.game_start(), 'Поздравляем! Игра завершена. Сокровище найдено. \n Ваш промокод SUPER100')


if __name__ == '__test_Game_class__':
    unittest.main()