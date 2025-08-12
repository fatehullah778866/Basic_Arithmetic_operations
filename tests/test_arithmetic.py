import math
import pytest

import basic_python_arithmetic_operations as arith


def test_add():
    assert arith.add(4, 7) == 11


def test_subtract():
    assert arith.subtract(4, 7) == -3


def test_multiply():
    assert arith.multiply(4, 7) == 28


def test_divide():
    assert arith.divide(14, 7) == 2


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        arith.divide(1, 0)