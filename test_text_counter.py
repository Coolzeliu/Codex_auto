import unittest

from text_counter import count_text


class TextCounterTest(unittest.TestCase):
    def test_english_text(self) -> None:
        self.assertEqual(
            count_text("Hello Codex"),
            {"characters": 11, "non_whitespace_characters": 10, "words": 2},
        )

    def test_chinese_text(self) -> None:
        self.assertEqual(
            count_text("你好 世界"),
            {"characters": 5, "non_whitespace_characters": 4, "words": 2},
        )


if __name__ == "__main__":
    unittest.main()
