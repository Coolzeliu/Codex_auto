import unittest

from calculator import add, subtract


class CalculatorTest(unittest.TestCase):
    def test_add(self) -> None:
        self.assertEqual(add(3, 2), 5)

    def test_subtract(self) -> None:
        self.assertEqual(subtract(3, 2), 1)


if __name__ == "__main__":
    unittest.main()
