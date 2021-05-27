class Calculator(object):

    @classmethod
    def add(cls, num1: int, num2: int):
        return num1 + num2

    @classmethod
    def subtract(cls, param: int, param1: int):
        return param - param1

    @classmethod
    def multiply(cls, param: int, param1: int):
        if isinstance(param, int) and isinstance(param1, int):
            return param * param1
        else:
            raise TypeError()

    @classmethod
    def divide(cls, param, param1):
        return param // param1
