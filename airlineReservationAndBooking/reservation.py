class Reservation(object):
    __reserved_passengers = []

    def reserve_flight(self, passenger, seat_class):
        self.__reserved_passengers.append(passenger)
        passenger.set_seat_class(seat_class)

    def has_reserved(self, passenger):
        has_reserved = False
        for i in self.__reserved_passengers:
            if i == passenger:
                has_reserved = True
        return has_reserved

    def get_reservation_ID(self, passenger):
        reservation_id = None
        index = 0

        while index < len(self.__reserved_passengers):
            if self.__reserved_passengers[index] == passenger:
                reservation_id = index + 1
                break
            index += 1
        return reservation_id

    def get_reserved_seat_class(self, passenger):
        seat_class = None
        index = 0

        while index < len(self.__reserved_passengers):
            if self.__reserved_passengers[index] == passenger:
                seat_class = passenger.get_seat_class()
                break
            index += 1
        return seat_class

    def get_total_number_reserved_seats(self):
        return len(self.__reserved_passengers)

    def cancelReservation(self, reservation_id):
        index = 1
        while index <= len(self.__reserved_passengers):
            if index == reservation_id:
                del self.__reserved_passengers[index - 1]
                break
        index += 1

    @classmethod
    def get_reserved_passengers(cls):
        return cls.__reserved_passengers

    def empty_reservation_list(self):
        self.__reserved_passengers.clear()

    @classmethod
    def get_passenger(cls, reservation_id):
        for i in range(len(cls.__reserved_passengers)):
            if i + 1 == reservation_id:
                return cls.__reserved_passengers[i]
