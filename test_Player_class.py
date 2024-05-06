import unittest
from Player_class import Player


class TestPlayer(unittest.TestCase):
    def test_new_point(self):
        player = Player(12)
        self.assertEqual(player.new_point([8, 'H']),[1, 'Введены координаты (8, H)'])

    def test_new_fail(self):
        player = Player(12)
        self.assertEqual(player.new_point([11, 'H']),[0, "Ошибка! Число должно быть от 1 до 10"])

    def test_new_fail_letter(self):
        player = Player(12)
        self.assertEqual(player.new_point([10, 'X']),[0, "Ошибка! Буква должна быть в диапазоне от A до J"])


if __name__ == '__test_Player_class__':
    unittest.main()