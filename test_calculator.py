import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    # Test cases for add()
    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_add_negative(self):
        self.assertEqual(self.calc.add(-1, -2), -3)

    # Test cases for subtract()
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)

    def test_subtract_negative(self):
        self.assertEqual(self.calc.subtract(-5, -2), -3)

    # Test cases for multiply()
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 7), 21)

    def test_multiply_with_zero(self):
        self.assertEqual(self.calc.multiply(3, 0), 0)

    # Test cases for divide()
    def test_divide(self):
        self.assertEqual(self.calc.divide(5, 2), 2)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)

    # Test cases for modulo()
    def test_modulo(self):
        self.assertEqual(self.calc.modulo(5, 2), 1)

    def test_modulo_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.modulo(5, 0)

if __name__ == '__main__':
    unittest.main()