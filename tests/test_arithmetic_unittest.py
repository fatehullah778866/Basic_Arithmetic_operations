import unittest

import basic_python_arithmetic_operations as arith


class TestArithmetic(unittest.TestCase):
    def test_add(self):
        self.assertEqual(arith.add(4, 7), 11)

    def test_subtract(self):
        self.assertEqual(arith.subtract(4, 7), -3)

    def test_multiply(self):
        self.assertEqual(arith.multiply(4, 7), 28)

    def test_divide(self):
        self.assertEqual(arith.divide(14, 7), 2)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            arith.divide(1, 0)


if __name__ == "__main__":
    unittest.main()