from airlineReservationAndBooking.reservation import Reservation


class FlightBooking(object):
    booked_seats = []

    def book_with_reservation_id(self, reservation_id):
        reserved_passenger = Reservation.get_passenger(reservation_id)
        if reserved_passenger.get_seat_class() == "FIRSTCLASS":
            seat_count = self.get_total_number_of_first_class_seats_booked()
            if seat_count < 10 and not self.__passenger_has_booked(reserved_passenger):
                self.booked_seats.append(reserved_passenger)
                reserved_passenger.set_booked_status(True)
                seat_number = seat_count + 1
                reserved_passenger.assign_seat_number(seat_number)
            else:
                return "No available first class seats"

        elif reserved_passenger.get_seat_class() == "BUSINESS":
            seat_count = self.get_total_number_of_business_class_seats_booked()
            if seat_count < 20 and not self.__passenger_has_booked(reserved_passenger):
                self.booked_seats.append(reserved_passenger)
                reserved_passenger.set_booked_status(True)
                seat_number = seat_count + 11
                reserved_passenger.assign_seat_number(seat_number)
            else:
                return "No available Business class seats"

        elif reserved_passenger.get_seat_class() == "ECONOMY":
            seat_count = self.get_total_number_of_economy_class_seats_booked()
            if seat_count < 20 and not self.__passenger_has_booked(reserved_passenger):
                self.booked_seats.append(reserved_passenger)
                reserved_passenger.set_booked_status(True)
                seat_number = seat_count + 31
                reserved_passenger.assign_seat_number(seat_number)
            else:
                return "No available Economy class seats"

    def get_total_count_of_seats_booked(self):
        return len(self.booked_seats)

    @classmethod
    def get_booked_seat_type(cls, passenger):
        for booked_passenger in cls.booked_seats:
            if booked_passenger == passenger:
                return booked_passenger.get_seat_class()

    def __passenger_has_booked(self, passenger):
        passenger_has_booked = False
        for i in self.booked_seats:
            if i == passenger:
                passenger_has_booked = True
                break
        return passenger_has_booked

    def book_flight(self, passenger, seat_class):
        if seat_class == "FIRSTCLASS":
            seat_count = self.get_total_number_of_first_class_seats_booked()
            if seat_count < 10:
                if not self.__passenger_has_booked(passenger):
                    self.booked_seats.append(passenger)
                    passenger.set_seat_class(seat_class)
                    passenger.set_booked_status(True)
                    seat_number = seat_count + 1
                    passenger.assign_seat_number(seat_number)
            else:
                return "No available first class seats"

        elif seat_class == "BUSINESS":
            seat_count = self.get_total_number_of_business_class_seats_booked()
            if seat_count < 10:
                if not self.__passenger_has_booked(passenger):
                    self.booked_seats.append(passenger)
                    passenger.set_seat_class(seat_class)
                    passenger.set_booked_status(True)
                    seat_number = seat_count + 11
                    passenger.assign_seat_number(seat_number)
            else:
                return "No available Business class seats"

        elif seat_class == "ECONOMY":
            seat_count = self.get_total_number_of_economy_class_seats_booked()
            if seat_count < 10:
                if not self.__passenger_has_booked(passenger):
                    self.booked_seats.append(passenger)
                    passenger.set_seat_class(seat_class)
                    passenger.set_booked_status(True)
                    seat_number = seat_count + 31
                    passenger.assign_seat_number(seat_number)
            else:
                return "No available economy class seats"

    def get_total_number_of_first_class_seats_booked(self):
        counter = 0
        for passenger in self.booked_seats:
            if passenger.get_seat_class() == "FIRSTCLASS":
                counter += 1
        return counter

    def get_total_number_of_business_class_seats_booked(self):
        counter = 0
        for passenger in self.booked_seats:
            if passenger.get_seat_class() == "BUSINESS":
                counter += 1
        return counter

    def get_total_number_of_economy_class_seats_booked(self):
        counter = 0
        for passenger in self.booked_seats:
            if passenger.get_seat_class() == "ECONOMY":
                counter += 1
        return counter

    def empty_booked_list(self):
        self.booked_seats.clear()

    @classmethod
    def get_passenger_booked_seat_type(cls, passenger):
        for booked_passenger in cls.booked_seats:
            if booked_passenger == passenger:
                return booked_passenger.get_seat_class()

    @classmethod
    def get_booked_seats(cls):
        return cls.booked_seats
