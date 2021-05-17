import unittest
from airlineReservationAndBooking.airline import Airline
from airlineReservationAndBooking.aeroplane import Aeroplane
from airlineReservationAndBooking.Passenger import Passenger
from airlineReservationAndBooking.reservation import Reservation
from airlineReservationAndBooking.SeatClass import SeatClass
from airlineReservationAndBooking.flightbooking import FlightBooking
from airlineReservationAndBooking.payment import Payment
from airlineReservationAndBooking.payment_type import PaymentType


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.aeroplane = Aeroplane("Eagle squad")
        self.airline = Airline("Imperial Airline", self.aeroplane)
        self.reservation = Reservation()
        self.passenger = Passenger("Olu Jola", "0000", "bina@jolo.com")
        self.flight_booking = FlightBooking()
        self.payment = Payment()

    def tearDown(self) -> None:
        self.reservation.empty_reservation_list()
        self.flight_booking.empty_booked_list()

    def test_that_airline_can_be_created(self):
        self.assertEqual("Airline name: Imperial Airline" +
                         "\nNumber of aeroplanes: 1", self.airline.__str__())

    def test_that_airline_can_have_aeroplanes(self):
        self.assertEqual(1, self.airline.get_total_number_of_aeroplanes())
        second_aeroplane = Aeroplane
        self.airline.acquireAeroplane(second_aeroplane)
        self.assertEqual(2, self.airline.get_total_number_of_aeroplanes())

    def test_that_aeroplane_has_fifty_seats(self):
        self.assertEqual(50, self.aeroplane.get_total_number_of_seats())

    def test_first_class_reservation(self):
        self.reservation.reserve_flight(self.passenger, SeatClass.first_class)
        self.assertTrue(self.reservation.has_reserved(self.passenger))
        self.assertEqual(1, self.reservation.get_reservation_ID(self.passenger))
        self.assertEqual("FIRSTCLASS", self.reservation.get_reserved_seat_class(self.passenger))

    def test_business_class_reservation(self):
        self.reservation.reserve_flight(self.passenger, SeatClass.business)
        self.assertTrue(self.reservation.has_reserved(self.passenger))
        self.assertEqual(1, self.reservation.get_reservation_ID(self.passenger))
        self.assertEqual("BUSINESS", self.reservation.get_reserved_seat_class(self.passenger))

    def test_economy_class_reservation(self):
        self.reservation.reserve_flight(self.passenger, SeatClass.economy)
        self.assertTrue(self.reservation.has_reserved(self.passenger))
        self.assertEqual(1, self.reservation.get_reservation_ID(self.passenger))
        self.assertEqual("ECONOMY", self.reservation.get_reserved_seat_class(self.passenger))

    def test_multiple_passenger_can_reserve_first_class(self):
        self.passenger1 = Passenger("Ade Bajomo", "23543", "dbomo@gmail.com")
        self.reservation.reserve_flight(self.passenger, SeatClass.first_class)
        self.reservation.reserve_flight(self.passenger1, SeatClass.first_class)
        self.assertTrue(self.reservation.has_reserved(self.passenger))
        self.assertTrue(self.reservation.has_reserved(self.passenger1))
        self.assertEqual(1, self.reservation.get_reservation_ID(self.passenger))
        self.assertEqual(2, self.reservation.get_reservation_ID(self.passenger1))
        self.assertEqual("FIRSTCLASS", self.reservation.get_reserved_seat_class(self.passenger))
        self.assertEqual("FIRSTCLASS", self.reservation.get_reserved_seat_class(self.passenger1))
        self.assertEqual(2, self.reservation.get_total_number_reserved_seats())

    def test_multiple_passenger_can_reserve_business_class(self):
        self.passenger1 = Passenger("Ade Bajomo", "23543", "dbomo@gmail.com")
        self.reservation.reserve_flight(self.passenger, SeatClass.business)
        self.reservation.reserve_flight(self.passenger1, SeatClass.business)
        self.assertTrue(self.reservation.has_reserved(self.passenger))
        self.assertTrue(self.reservation.has_reserved(self.passenger1))
        self.assertEqual(1, self.reservation.get_reservation_ID(self.passenger))
        self.assertEqual(2, self.reservation.get_reservation_ID(self.passenger1))
        self.assertEqual("BUSINESS", self.reservation.get_reserved_seat_class(self.passenger))
        self.assertEqual("BUSINESS", self.reservation.get_reserved_seat_class(self.passenger1))
        self.assertEqual(2, self.reservation.get_total_number_reserved_seats())

    def test_multiple_passenger_can_reserve_economy_class(self):
        self.passenger1 = Passenger("Ade Bajomo", "23543", "dbomo@gmail.com")
        self.reservation.reserve_flight(self.passenger, SeatClass.economy)
        self.reservation.reserve_flight(self.passenger1, SeatClass.economy)
        self.assertTrue(self.reservation.has_reserved(self.passenger))
        self.assertTrue(self.reservation.has_reserved(self.passenger1))
        self.assertEqual(1, self.reservation.get_reservation_ID(self.passenger))
        self.assertEqual(2, self.reservation.get_reservation_ID(self.passenger1))
        self.assertEqual("ECONOMY", self.reservation.get_reserved_seat_class(self.passenger))
        self.assertEqual("ECONOMY", self.reservation.get_reserved_seat_class(self.passenger1))
        self.assertEqual(2, self.reservation.get_total_number_reserved_seats())

    def test_that_passenger_can_cancel_reservation(self):
        self.reservation.reserve_flight(self.passenger, SeatClass.economy)
        self.assertTrue(self.reservation.has_reserved(self.passenger))
        self.assertEqual(1, self.reservation.get_reservation_ID(self.passenger))
        self.assertEqual("ECONOMY", self.reservation.get_reserved_seat_class(self.passenger))
        reservation_id = self.reservation.get_reservation_ID(self.passenger)
        self.reservation.cancelReservation(reservation_id)
        self.assertFalse(self.reservation.has_reserved(self.passenger))
        self.assertEqual(0, self.reservation.get_total_number_reserved_seats())
        self.assertIsNone(self.reservation.get_reserved_seat_class(self.passenger))

    def test_that_passenger_can_book_first_class_with_reservation_id(self):
        self.reservation.reserve_flight(self.passenger, SeatClass.first_class)
        self.assertEqual(1, self.reservation.get_total_number_reserved_seats())
        reservation_id = self.reservation.get_reservation_ID(self.passenger)
        self.flight_booking.book_with_reservation_id(reservation_id)
        self.assertEqual(1, self.flight_booking.get_total_count_of_seats_booked())
        self.assertEqual("FIRSTCLASS", FlightBooking.get_booked_seat_type(self.passenger))

    def test_that_passenger_can_book_economy_class_with_reservation_id(self):
        self.reservation.reserve_flight(self.passenger, SeatClass.economy)
        self.passenger1 = Passenger("Ade Bajomo", "23543", "dbomo@gmail.com")
        self.reservation.reserve_flight(self.passenger1, SeatClass.first_class)
        self.assertEqual(2, self.reservation.get_total_number_reserved_seats())
        reservation_id = self.reservation.get_reservation_ID(self.passenger)
        self.flight_booking.book_with_reservation_id(reservation_id)
        self.assertEqual(1, self.flight_booking.get_total_count_of_seats_booked())
        self.assertEqual("ECONOMY", FlightBooking.get_booked_seat_type(self.passenger))

    def test_that_passenger_can_book_business_class_with_reservation_id(self):
        self.reservation.reserve_flight(self.passenger, SeatClass.business)
        self.assertEqual(1, self.reservation.get_total_number_reserved_seats())
        reservation_id = self.reservation.get_reservation_ID(self.passenger)
        self.flight_booking.book_with_reservation_id(reservation_id)
        self.assertEqual(1, self.flight_booking.get_total_number_of_business_class_seats_booked())
        self.assertEqual(1, self.flight_booking.get_total_count_of_seats_booked())
        self.assertEqual("BUSINESS", FlightBooking.get_booked_seat_type(self.passenger))

    def test_that_same_reservation_id_cannot_be_used_to_book_a_flight_twice(self):
        self.reservation.reserve_flight(self.passenger, SeatClass.first_class)
        self.assertEqual(1, self.reservation.get_total_number_reserved_seats())
        reservation_id = self.reservation.get_reservation_ID(self.passenger)
        self.flight_booking.book_with_reservation_id(reservation_id)
        self.assertEqual(1, self.flight_booking.get_total_count_of_seats_booked())
        self.assertEqual("FIRSTCLASS", FlightBooking.get_booked_seat_type(self.passenger))

        self.flight_booking.book_with_reservation_id(reservation_id)
        self.assertEqual(1, self.flight_booking.get_total_count_of_seats_booked())

    def test_that_passenger_can_book_first_class_without_first_reserving_seat(self):
        self.flight_booking.book_flight(self.passenger, SeatClass.first_class)
        self.assertEqual(1, self.flight_booking.get_total_count_of_seats_booked())
        self.assertEqual("FIRSTCLASS", FlightBooking.get_booked_seat_type(self.passenger))

    def test_that_passenger_can_book_business_class_without_first_reserving_seat(self):
        self.flight_booking.book_flight(self.passenger, SeatClass.business)
        self.assertEqual(1, self.flight_booking.get_total_count_of_seats_booked())
        self.assertEqual("BUSINESS", FlightBooking.get_booked_seat_type(self.passenger))

    def test_that_passenger_can_book_economy_class_without_first_reserving_seat(self):
        self.flight_booking.book_flight(self.passenger, SeatClass.economy)
        self.assertEqual(1, self.flight_booking.get_total_count_of_seats_booked())
        self.assertEqual("ECONOMY", FlightBooking.get_booked_seat_type(self.passenger))

    def test_that_only_ten_first_class_seats_can_be_booked(self):
        passenger_1 = Passenger("Olu Jola", "0000", "bina@jolo.com")
        passenger_2 = Passenger("Olu Jola", "0000", "bina@jolo.com")
        passenger_3 = Passenger("Olu Jola", "0000", "bina@jolo.com")
        passenger_4 = Passenger("Olu Jola", "0000", "bina@jolo.com")
        passenger_5 = Passenger("Olu Jola", "0000", "bina@jolo.com")
        passenger_6 = Passenger("Olu Jola", "0000", "bina@jolo.com")
        passenger_7 = Passenger("Olu Jola", "0000", "bina@jolo.com")
        passenger_8 = Passenger("Olu Jola", "0000", "bina@jolo.com")
        passenger_9 = Passenger("Olu Jola", "0000", "bina@jolo.com")
        passenger_10 = Passenger("Olu Jola", "0000", "bina@jolo.com")
        passenger_11 = Passenger("Olu Jola", "0000", "bina@jolo.com")

        self.flight_booking.book_flight(passenger_1, SeatClass.first_class)
        self.flight_booking.book_flight(passenger_2, SeatClass.first_class)
        self.flight_booking.book_flight(passenger_3, SeatClass.first_class)
        self.flight_booking.book_flight(passenger_4, SeatClass.first_class)
        self.flight_booking.book_flight(passenger_5, SeatClass.first_class)
        self.flight_booking.book_flight(passenger_6, SeatClass.first_class)
        self.flight_booking.book_flight(passenger_7, SeatClass.first_class)
        self.flight_booking.book_flight(passenger_8, SeatClass.first_class)
        self.flight_booking.book_flight(passenger_9, SeatClass.first_class)
        self.flight_booking.book_flight(passenger_10, SeatClass.first_class)
        self.flight_booking.book_flight(passenger_11, SeatClass.first_class)

        self.assertEqual(10, self.flight_booking.get_total_number_of_first_class_seats_booked())
        self.assertEqual(10, self.flight_booking.get_total_count_of_seats_booked())

    def test_that_airline_can_set_the_price_of_first_class_booking_pass(self):
        self.airline.set_price_of_first_class(1000)
        self.assertEqual(1000, self.airline.get_price_of_first_class_seat())

    def test_that_airline_can_set_the_price_of_business_class_booking_pass(self):
        self.airline.set_price_of_business_class(700)
        self.assertEqual(700, self.airline.get_price_of_business_class_seat())

    def test_that_airline_can_set_the_price_of_economy_class_booking_pass(self):
        self.airline.set_price_of_business_class(500)
        self.assertEqual(500, self.airline.get_price_of_business_class_seat())

    def test_that_passenger_can_make_payment_for_first_class_booking_pass(self):
        self.flight_booking.book_flight(self.passenger, SeatClass.first_class)
        self.assertEqual(1, self.flight_booking.get_total_number_of_first_class_seats_booked())
        self.assertEqual(SeatClass.first_class, FlightBooking.get_passenger_booked_seat_type(self.passenger))
        self.airline.set_price_of_first_class(1000)
        self.assertEqual(1000, self.airline.get_price_of_first_class_seat())

        self.payment.make_payment(self.passenger, 1000, SeatClass.first_class, PaymentType.master_card)

        self.assertTrue(self.passenger.has_paid())
        self.assertEqual(PaymentType.master_card, self.passenger.get_payment_type())
