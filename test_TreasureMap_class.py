import unittest
from TreasureMap_class import TreasureMap


class TestTreasureMap(unittest.TestCase):
    def test_check_position(self):
        my_map = TreasureMap()
        my_map.x = 1
        my_map.y = 'A'
        self.assertEqual(my_map.check_position(10, 'H'), [0, 'Вы пока не нашли сокровище'])

    def test_check_position_fail_y(self):
        my_map = TreasureMap()
        my_map.x = 7
        my_map.y = 'F'
        self.assertEqual(my_map.check_position(8, 'H'), [1, 'Вы близко к сокровищу!'])

    def test_check_position_soclose(self):
        my_map = TreasureMap()
        my_map.x = 7
        my_map.y = 'H'
        self.assertEqual(my_map.check_position(8, 'H'), [1, 'Вы близко к сокровищу!'])

    def test_check_position_soclose_x(self):
        my_map = TreasureMap()
        my_map.x = 7
        my_map.y = 'F'
        self.assertEqual(my_map.check_position(7, 'H'), [1, 'Вы близко к сокровищу!'])

    def test_check_position_win(self):
        my_map = TreasureMap()
        my_map.x = 7
        my_map.y = 'H'
        self.assertEqual(my_map.check_position(7, 'H'), [2, f'Поздравляем! Игра завершена. Сокровище найдено. \n Ваш промокод SUPER100'])

    def test_check_position_fail(self):
        my_map = TreasureMap()
        my_map.x = 10
        my_map.y = 'A'
        self.assertEqual(my_map.check_position(10, 'H'), [0, 'Вы пока не нашли сокровище'])


if __name__ == '__test_TreasureMap_class__':
    unittest.main()