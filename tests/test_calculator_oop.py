import unittest
from calculator.calculator_oop import Calculator


class CalculatorTest(unittest.TestCase):

    def test_oop_add(self):
        self.assertEqual(9, Calculator.add(4, 5))

    def test_add_result_type(self):
        self.assertIsInstance(Calculator.add(2, 3), int)

    def test_add_non_int_type(self):
        with self.assertRaises(TypeError):
            Calculator.add("1", 1)

    def test_illegal_additional_argument(self):
        with self.assertRaises(TypeError):
            self.assertEqual(Calculator.add(1, -7, 5), -6)

    def test_calculator_can_subtract_two_Numbers(self):
        self.assertEqual(Calculator.subtract(8, 3), 5)
        self.assertEqual(Calculator.subtract(-5, 3), -8)
        self.assertEqual(Calculator.subtract(1, -6), 7)

    def test_subtract_result_type(self):
        self.assertIsInstance(Calculator.subtract(2, 3), int)

    def test_subtract_non_int_type(self):
        with self.assertRaises(TypeError):
            Calculator.subtract("1", 1)

    def test_illegal_subtraction_argument(self):
        with self.assertRaises(TypeError):
            self.assertEqual(Calculator.subtract(1, -7, 5), -6)

    def test_calculator_can_multiply_two_Numbers(self):
        self.assertEqual(Calculator.multiply(8, 3), 24)
        self.assertEqual(Calculator.multiply(-5, 3), -15)
        self.assertEqual(Calculator.multiply(1, -6), -6)

    def test_multiply_result_type(self):
        self.assertIsInstance(Calculator.multiply(2, 3), int)

    def test_multiply_non_int_type(self):
        with self.assertRaises(TypeError):
            Calculator.multiply("1", 1)

    def test_illegal_multiplication_argument(self):
        with self.assertRaises(TypeError):
            self.assertEqual(Calculator.multiply(1, -7, 5), -6)

    def test_calculator_can_divide_two_Numbers(self):
        self.assertEqual(Calculator.divide(8, 2), 4)
        self.assertEqual(Calculator.divide(-15, 3), -5)
        self.assertEqual(Calculator.divide(12, -6), -2)

    def test_divide_result_type(self):
        self.assertIsInstance(Calculator.divide(12, 3), int)

    def test_division_non_int_type(self):
        with self.assertRaises(TypeError):
            Calculator.divide("1", 1)

    def test_illegal_division_argument(self):
        with self.assertRaises(TypeError):
            self.assertEqual(Calculator.divide(14, -7, 5), -2)