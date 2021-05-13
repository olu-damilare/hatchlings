class Passenger(object):

    def __init__(self, name, phone_number, email_address):
        self.__name = name
        self.__phone_number = phone_number
        self.__email_address = email_address

    def set_seat_class(self, seat_class):
        self.__seat_class = seat_class

    def get_seat_class(self):
        return self.__seat_class
