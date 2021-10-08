import unittest
from main import add, get_value


class CalcTester(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(9, add(4, 5))

    def test_add_negative_numbers(self):
        self.assertEqual(-9, add(-4, -5))

    def test_add_negative_and_positive_numbers(self):
        self.assertEqual(-1, add(4, -5))

    def test_range_values(self):
        values = [get_value() for _ in range(1000000)]
        check = [value in range(1, 10) for value in values]
        self.assertTrue(all(check))


if __name__ == '__main__':
    unittest.main()
