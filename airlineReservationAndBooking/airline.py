from airlineReservationAndBooking.aeroplane import Aeroplane
from airlineReservationAndBooking.flight_details import FlightDetails


class Airline(object):
    __first_class_seat_price = None
    __business_class_seat_price = None
    __economy_class_seat_price = None

    def __init__(self, airline_name: str, aeroplane: Aeroplane):
        self.__aeroplanes = []
        self.__flight_details = []
        self.__airlineName = airline_name
        self.__aeroplanes.append(aeroplane)


    def get_airline_name(self):
        return self.__airlineName

    def __str__(self):
        return "Airline name: " + self.get_airline_name() + "\nNumber of aeroplanes: " + str(self.get_total_number_of_aeroplanes())

    def get_total_number_of_aeroplanes(self):
        return len(self.__aeroplanes)

    def acquireAeroplane(self, aeroplane):
        self.__aeroplanes.append(aeroplane)

    @classmethod
    def set_price_of_first_class(cls, amount):
        cls.__first_class_seat_price = amount

    @classmethod
    def get_price_of_first_class_seat(cls):
        return cls.__first_class_seat_price

    @classmethod
    def set_price_of_business_class(cls, amount):
        cls.__business_class_seat_price = amount

    @classmethod
    def get_price_of_business_class_seat(cls):
        return cls.__business_class_seat_price

    @classmethod
    def set_price_of_economy_class(cls, amount):
        cls.__economy_class_seat_price = amount

    @classmethod
    def get_price_of_economy_class_seat(cls):
        return cls.__economy_class_seat_price

    def generate_flight_number(self):
        details = FlightDetails()
        details.assign_flight_number(len(self.__flight_details) + 1)
        self.__flight_details.append(details)

        return len(self.__flight_details)

    def assign_pilot(self, pilot, flight_number):
        for flight_details in self.__flight_details:
            if flight_details.get_flight_number() == flight_number:
                flight_details.record_pilot_info(pilot)

    def assign_host(self, host, flight_number):
        for flight_details in self.__flight_details:
            if flight_details.get_flight_number() == flight_number:
                flight_details.record_host_info(host)

    def board_passenger(self, passenger, flight_number):
        for flight_details in self.__flight_details:
            if flight_details.get_flight_number() == flight_number:
                flight_details.record_passenger_info(passenger)

    def generate_flight_details(self, flight_number):
        for flight_details in self.__flight_details:
            if flight_details.get_flight_number() == flight_number:
                return flight_details.__str__()
            

