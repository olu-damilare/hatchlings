import unittest
from calculator.CalculatorFunctions import add, subtract, multiply, divide


class CalculatorFunctionTest(unittest.TestCase):
    def test_calculator_can_add_two_Numbers(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-5, 3), -2)
        self.assertEqual(add(1, -7), -6)

    def test_add_result_type(self):
        self.assertIsInstance(add(2, 3), int)

    def test_add_non_int_type(self):
        with self.assertRaises(TypeError):
            add("1", 1)

    def test_illegal_additional_argument(self):
        with self.assertRaises(TypeError):
            self.assertEqual(add(1, -7, 5), -6)

    def test_calculator_can_subtract_two_Numbers(self):
        self.assertEqual(subtract(8, 3), 5)
        self.assertEqual(subtract(-5, 3), -8)
        self.assertEqual(subtract(1, -6), 7)

    def test_subtract_result_type(self):
        self.assertIsInstance(subtract(2, 3), int)

    def test_subtract_non_int_type(self):
        with self.assertRaises(TypeError):
            subtract("1", 1)

    def test_illegal_subtraction_argument(self):
        with self.assertRaises(TypeError):
            self.assertEqual(subtract(1, -7, 5), -6)

    def test_calculator_can_multiply_two_Numbers(self):
        self.assertEqual(multiply(8, 3), 24)
        self.assertEqual(multiply(-5, 3), -15)
        self.assertEqual(multiply(1, -6), -6)

    def test_multiply_result_type(self):
        self.assertIsInstance(multiply(2, 3), int)

    def test_multiply_non_int_type(self):
        with self.assertRaises(TypeError):
            multiply("1", 1)

    def test_illegal_multiplication_argument(self):
        with self.assertRaises(TypeError):
            self.assertEqual(multiply(1, -7, 5), -6)

    def test_calculator_can_divide_two_Numbers(self):
        self.assertEqual(divide(8, 2), 4)
        self.assertEqual(divide(-15, 3), -5)
        self.assertEqual(divide(12, -6), -2)

    def test_divide_result_type(self):
        self.assertIsInstance(divide(12, 3), int)

    def test_division_non_int_type(self):
        with self.assertRaises(TypeError):
            divide("1", 1)

    def test_illegal_division_argument(self):
        with self.assertRaises(TypeError):
            self.assertEqual(divide(14, -7, 5), -2)


if __name__ == '__main__':
    unittest.main()
