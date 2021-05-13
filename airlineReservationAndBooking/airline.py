from airlineReservationAndBooking.aeroplane import Aeroplane


class Airline(object):

    def __init__(self, airline_name: str, aeroplane: Aeroplane):
        self.__aeroplanes = []
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

