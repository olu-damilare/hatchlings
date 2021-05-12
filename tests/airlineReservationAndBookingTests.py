import unittest
from airlineReservationAndBooking.airline import Airline
from airlineReservationAndBooking.aeroplane import Aeroplane
from airlineReservationAndBooking.Passenger import Passenger
from airlineReservationAndBooking.reservation import Reservation
from airlineReservationAndBooking.SeatClass import SeatClass


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.aeroplane = Aeroplane("Eagle squad")
        self.airline = Airline("Imperial Airline", self.aeroplane)
        self.reservation = Reservation()

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
        self.passenger = Passenger("Olu Jola", "0000", "bina@jolo.com")
        self.reserve = self.reservation.reserve_flight(self.passenger, SeatClass.first_class)
        self.assertTrue(self.reservation.has_reserved(self.passenger))
        self.assertEqual(1, self.reservation.get_reservation_ID(self.passenger))
        self.assertEqual("FIRSTCLASS", self.reservation.get_reserved_seat_class(self.passenger))
