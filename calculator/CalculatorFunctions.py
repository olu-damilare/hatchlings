def add(first_number: int, second_number: int):
    return first_number + second_number


def subtract(first_number: int, second_number: int):
    return first_number - second_number


def multiply(first_number: int, second_number: int):
    if isinstance(first_number, int) and isinstance(second_number, int):
        return first_number * second_number
    else:
        raise TypeError(print("number must be of int type"))


def divide(first_number: int, second_number: int):
    return int(first_number / second_number)
