#!/usr/bin/env python3
"""A small command-line multiplication program."""

import argparse


def multiply(left: float, right: float) -> float:
    """Return the product of two numbers."""
    return left * right


def format_number(value: float) -> str:
    """Display whole-number results without a trailing .0."""
    return str(int(value)) if value.is_integer() else str(value)


def main() -> None:
    parser = argparse.ArgumentParser(description="计算两个数字的乘积")
    parser.add_argument("left", type=float, help="第一个数字")
    parser.add_argument("right", type=float, help="第二个数字")
    args = parser.parse_args()

    print(format_number(multiply(args.left, args.right)))


if __name__ == "__main__":
    main()
