import unittest
from credit_card.validation import CreditCardValidation


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.credit_card_number = 4388576018402626
        self.validate = CreditCardValidation()

    def test_thatTheSumOfDoubleOfEvenPositionsCanBeObtained(self):
        self.assertEqual(37, self.validate.calculate_sum_of_double_even_place(self.credit_card_number))

    def test_that_the_sum_of_odd_positions_can_be_obtained(self):
        self.assertEqual(38, self.validate.calculate_sum_of_odd_place(self.credit_card_number))

    def testThatCreditCardIsInvalid(self):
        self.assertFalse(self.validate.isValid(self.credit_card_number))
        self.assertTrue(self.validate.isValid(371175520987141))

