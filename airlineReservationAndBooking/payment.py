from airlineReservationAndBooking.airline import Airline


class Payment(object):
    def make_payment(self, passenger, amount, seat_class, payment_type):
        has_paid = False
        if passenger.has_booked():
            if seat_class == "FIRSTCLASS":
                if amount >= Airline.get_price_of_first_class_seat():
                    has_paid = True
                    passenger.set_payment_type(payment_type)

            elif seat_class == "BUSINESS":
                if amount >= Airline.get_price_of_business_class_seat():
                    has_paid = True
                    passenger.set_payment_type(payment_type)

            elif seat_class == "ECONOMY":
                if amount >= Airline.get_price_of_economy_class_seat():
                    has_paid = True
                    passenger.set_payment_type(payment_type)
            passenger.make_payment(has_paid)