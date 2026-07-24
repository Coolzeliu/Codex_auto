#!/usr/bin/env python3
"""Count characters and words in text or a UTF-8 text file."""

import argparse
from pathlib import Path


def count_text(text: str) -> dict[str, int]:
    """Return basic statistics for the supplied text."""
    return {
        "characters": len(text),
        "non_whitespace_characters": sum(not char.isspace() for char in text),
        "words": len(text.split()),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="统计文本的字符数和单词数")
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("text", nargs="?", help="需要统计的文本")
    source.add_argument("--file", type=Path, help="需要统计的 UTF-8 文本文件")
    args = parser.parse_args()

    text = args.file.read_text(encoding="utf-8") if args.file else args.text
    result = count_text(text)

    print(f"字符数: {result['characters']}")
    print(f"非空字符数: {result['non_whitespace_characters']}")
    print(f"单词数: {result['words']}")


if __name__ == "__main__":
    main()
