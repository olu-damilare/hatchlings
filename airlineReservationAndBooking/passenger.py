class Passenger(object):

    def __init__(self, name, phone_number, email_address):
        self.__name = name
        self.__phone_number = phone_number
        self.__email_address = email_address
        self.__payment_type = None
        self.__seat_class = None
        self.__paid = False
        self.__is_booked = False
        self.__seat_number = 0

    def set_seat_class(self, seat_class):
        self.__seat_class = seat_class

    def get_seat_class(self):
        return self.__seat_class

    def set_payment_type(self, payment_type):
        self.__payment_type = payment_type

    def get_payment_type(self):
        return self.__payment_type

    def has_paid(self):
        return self.__paid

    def set_booked_status(self, booked):
        self.__is_booked = booked

    def has_booked(self):
        return self.__is_booked

    def assign_seat_number(self, seat_number):
        self.__seat_number = seat_number

    def make_payment(self, has_paid):
        self.__paid = has_paid

    def __str__(self):
        return "Full Name = {}\nPhone number = {}\nEmail address = {}\nSeat class = {}\nSeat number = {}\nPayment " \
               "type = {}".format(self.__name, self.__phone_number, self.__email_address,
                                  self.__seat_class, self.__seat_number, self.__payment_type)

    def get_seat_number(self):
        return self.__seat_number
