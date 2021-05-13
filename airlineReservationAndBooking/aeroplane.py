from airlineReservationAndBooking.seat import Seat


class Aeroplane(object):

    def __init__(self, aeroplane_name: str, ):
        self.__seats = []
        self.__aeroplane_name = aeroplane_name
        seat = Seat()
        for i in range(50):
            self.__seats.append(seat)

    def get_total_number_of_seats(self):
        return len(self.__seats)

