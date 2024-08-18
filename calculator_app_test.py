# test_calculator.py
"""
    Provides tests for calculator app
"""
import unittest
from calculator_app import CalculatorApp

class TestCalculator(unittest.TestCase):
    """
    Provides some tests for calc app functions
    """

    def setUp(self):
        self.calc = CalculatorApp()


    def test_add(self):
        """
        Provides some tests for calc app functions
        """
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtract(self):
        """
        Provides some tests for calc app functions
        """
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(0, 5), -5)

    def test_multiply(self):
        """
        Provides some tests for calc app functions
        """
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, 5), -10)
        self.assertEqual(self.calc.multiply(0, 7), 0)

    def test_divide(self):
        """
        Provides some tests for calc app functions
        """
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)

        # Test division by zero
    def test_divide_by_zero(self):
        """
        Provides some tests for calc app functions
        """
        with self.assertRaises(ValueError):
            self.calc.divide(1, 0)

if __name__ == '__main__':
    unittest.main()
