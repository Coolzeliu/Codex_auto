#!/usr/bin/env python3
"""A tiny command-line calculator supporting addition and subtraction."""

import argparse


def add(left: float, right: float) -> float:
    """Return the sum of two numbers."""
    return left + right


def subtract(left: float, right: float) -> float:
    """Return the difference between two numbers."""
    return left - right


def format_number(value: float) -> str:
    """Avoid displaying a trailing .0 for integer results."""
    return str(int(value)) if value.is_integer() else str(value)


def main() -> None:
    parser = argparse.ArgumentParser(description="Add or subtract two numbers.")
    parser.add_argument("operation", choices=("add", "subtract"))
    parser.add_argument("left", type=float)
    parser.add_argument("right", type=float)
    args = parser.parse_args()

    operation = add if args.operation == "add" else subtract
    print(format_number(operation(args.left, args.right)))


if __name__ == "__main__":
    main()
