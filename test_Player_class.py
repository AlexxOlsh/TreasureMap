import unittest
import Player_class


class test_Player(unittest.TestCase):
    def test_process_numbers(self):
        self.assertEqual(process_numbers([1, 2, 3, 4, 5, -2, -4]),20)


if __name__ == '__test_main__':
    unittest.main()