class CreditCardValidation(object):

    def calculate_sum_of_double_even_place(self, credit_card_number):
        counter = len(str(credit_card_number)) - 2
        self.sum = 0
        while counter >= 0:
            temp_sum = 2 * int(str(credit_card_number)[counter])
            if temp_sum < 10:
                self.sum += temp_sum
            else:
                self.sum += (temp_sum // 10) + (temp_sum % 10)
            counter -= 2
        return self.sum

    def calculate_sum_of_odd_place(self, credit_card_number):
        counter = len(str(credit_card_number)) - 1
        self.sum = 0
        while counter >= 0:
            self.sum += int(str(credit_card_number)[counter])
            counter -= 2
        return self.sum

    def isValid(self, credit_card_number):
        return (self.calculate_sum_of_odd_place(credit_card_number) +
                self.calculate_sum_of_double_even_place(credit_card_number)) % 10 == 0
