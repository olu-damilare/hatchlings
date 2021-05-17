class FlightDetails(object):
    def __init__(self):
        self.__passenger_info = []

    def assign_flight_number(self, flight_number):
        self.__flight_number = flight_number

    def record_passenger_info(self, passenger):
        self.__passenger_info.append(passenger)

    def record_pilot_info(self, pilot):
        self.__pilot = pilot

    def record_host_info(self, host):
        self.__host = host

    def get_flight_number(self):
        return self.__flight_number

    def __str__(self):
        details = "Flight Details:\nNumber of passengers = " + str(len(self.__passenger_info)) + "\n\n"
        "Flight number = " + str(self.__flight_number)
        "Host Details = " + self.__host.__str__() + "\n\n"
        "Pilot Details = " + self.__pilot.__str__() + "\n\n"
        "Passengers Information:\n\n"

        for passenger in self.__passenger_info:
            details.join(passenger.__str__())
