import unittest
from TreasureMap_class import TreasureMap


class TestTreasureMap(unittest.TestCase):
    # def test_check_position(self):
    #     x = 1
    #     y = 'A'
    #     my_map = TreasureMap()
    #     self.assertEqual(my_map.check_position(10, 'H'), 'Вы пока не нашли сокровище')

    # def test_check_position_soclose(self):
    #     x = 7
    #     y = 'H'
    #     my_map = TreasureMap()
    #     self.assertEqual(my_map.check_position(8, 'H'), 'Вы близко к сокровищу!')
    #
    #
    def test_check_position_soclose_x(self):
        x = 7
        y = 'F'
        my_map = TreasureMap()
        self.assertEqual(my_map.check_position(7, 'H'), 'Вы близко к сокровищу!')
    #
    # def test_check_position_win(self):
    #     x = 7
    #     y = 'H'
    #     my_map = TreasureMap()
    #     self.assertEqual(my_map.check_position(7, 'H'), f'Поздравляем! Игра завершена. Сокровище найдено. \n Ваш промокод SUPER100')


if __name__ == '__test_TreasureMap_class__':
    unittest.main()