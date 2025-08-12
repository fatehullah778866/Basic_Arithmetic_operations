"""Basic arithmetic operations with a simple CLI.

Usage examples:
  python basic_python_arithmetic_operations.py 4 7           # compute all
  python basic_python_arithmetic_operations.py 4 7 --op add  # compute a single op
"""

from __future__ import annotations

import argparse
from typing import Callable


def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference of a and b (a - b)."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return the quotient of a divided by b.

    Raises:
        ZeroDivisionError: If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Division by zero is undefined.")
    return a / b


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Perform basic arithmetic operations on two numbers.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("a", type=float, help="First number")
    parser.add_argument("b", type=float, help="Second number")
    parser.add_argument(
        "--op",
        choices=["add", "sub", "mul", "div"],
        help="If omitted, all operations are computed.",
    )
    return parser


def main() -> None:
    parser = _build_parser()
    args = parser.parse_args()

    a: float = args.a
    b: float = args.b

    operation_map: dict[str, Callable[[float, float], float]] = {
        "add": add,
        "sub": subtract,
        "mul": multiply,
        "div": divide,
    }

    if args.op:
        func = operation_map[args.op]
        try:
            result = func(a, b)
        except ZeroDivisionError as error:
            print(f"Error: {error}")
            return
        print(result)
        return

    # Compute all operations when --op is not provided
    labels = {
        "add": "Addition",
        "sub": "Subtraction",
        "mul": "Multiplication",
        "div": "Division",
    }

    for key in ["add", "sub", "mul", "div"]:
        label = labels[key]
        try:
            value = operation_map[key](a, b)
            print(f"{label} is: {value}")
        except ZeroDivisionError as error:
            print(f"{label} error: {error}")


if __name__ == "__main__":
    main()
