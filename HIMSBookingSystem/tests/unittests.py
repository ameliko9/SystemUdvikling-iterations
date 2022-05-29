import unittest

from HIMSBookingSystem.Model.bookingmanager import BookingManager
from HIMSBookingSystem.Model.course import Course
from HIMSBookingSystem.Model.employee import Employee
from HIMSBookingSystem.Model.room import Room
from HIMSBookingSystem.Model.teacher import Teacher


t1 = Teacher(1, "Sofie", "Rasmussen", "SCIENCE", "SI", "Systemudvikling", 0)
t2 = Teacher(2, "Mette", "Olsen", "SUND", "SI", "Sygdomslærer", 4)
t3 = Teacher(3, "Henrik", "Hansen", "DTU", "ST", "Standarter", 3)

r1 = Room("Up1", 50, "SCIENCE", 0)
r2 = Room("A102", 20, "SCIENCE", 2)
r3 = Room("Aud.5", 100, "SUND", 4)

c1 = Course("SD-F22", "SI", "Sofie", 60, "Up1")
c2 = Course("SL-F22", "SI", "Mette", 90, "Aud.5")
c3 = Course("s-F22", "ST", "Henrik", 60, "DTU-5")


class TestEmployee(unittest.TestCase):
    def test_get_id(self):
        # Arrange
        e = Employee("UID42", "Ursula", "Gustav", "SUND", "CS")

        # Act
        actual = e.get_id()

        # Assert
        self.assertEqual(actual, "UID42")

    def test_get_name(self):
        # Arrange
        e = Employee("UID42", "Ursula", "Gustav", "SUND", "CS")

        # Act
        actual = e.get_name()

        # Assert
        self.assertEqual(actual, "Ursula Gustav")

    def test_get_education(self):
        # Arrange
        e = Employee("UID42", "Ursula", "Gustav", "SUND", "CS")

        # Act
        actual = e.get_education()

        # Assert
        self.assertEqual(actual, "CS")

    def test_get_campus(self):
        # Arrange
        e = Employee("UID42", "Ursula", "Gustav", "SUND", "CS")

        # Act
        actual = e.get_campus()

        # Assert
        self.assertEqual(actual, "SUND")


class TestTeacher(unittest.TestCase):
    pass


class BookingTest(unittest.TestCase):
    def test_makebooking(self):
        bm = BookingManager()
        booking1 = bm.make_booking(0, 8, "UP1", "Sys")
        self.assertIsNotNone(booking1)
        # Check booking1 matches what we inserted...

        booking2 = bm.get_booking(0, 8, "UP1")
        self.assertIsNotNone(booking2)
        # Check booking1 matches booking2...
        self.assertEqual(booking2.getCourse, "Sys")

if __name__ == '__main__':
    unittest.main()
