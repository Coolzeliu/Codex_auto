import unittest

from multiplication import multiply


class MultiplicationTest(unittest.TestCase):
    def test_positive_numbers(self) -> None:
        self.assertEqual(multiply(3, 4), 12)

    def test_negative_number(self) -> None:
        self.assertEqual(multiply(-2, 5), -10)

    def test_decimal_numbers(self) -> None:
        self.assertAlmostEqual(multiply(1.5, 2), 3.0)


if __name__ == "__main__":
    unittest.main()
