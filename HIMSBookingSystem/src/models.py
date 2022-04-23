# import datatime
# weekdays = ("Monday")
from enum import Enum

class RoomAvailability(Enum):
    Available = 1
    Busy = 0


class Weekday(Enum):
    Monday = 0
    Tuesday = 1
    Wednesday = 2
    Thursday = 3
    Friday = 4
    Saturday = 5
    Sunday = 6

class Education:
    def __init__(self, id, title, campus, duration, courses):
        self.id = id
        self.title = title
        self.campus = campus
        self.duration = duration
        self.courses = courses


class Employee:
    def __init__(self, id, firstname, lastname, campus, education):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.campus = campus
        self.education = education

    def get_name(self):
        return self.firstname + " " + self.lastname

    def get_id(self):
        return self.id

    def get_education(self):
        return self.education

    def get_campus(self):
        return self.campus


class Teacher(Employee):
    def __init__(self, id, firstname, lastname, campus, education, courses, calendar):
        super().__init__(id, firstname, lastname, campus, education)
        self.courses = courses
        self.calendar = Weekday.Monday

    def get_calendar(self):
        return self.calendar

    def book_room(self, booking_manager):
        pass


class Secretary(Employee):
    def __init__(self, id, name, faculty, education):
        super().__init__(id, name, faculty, education)

    def approve_booking(self):
        pass

class BookingConfirmation:
    pass


class BookingManager:
    def get_booking(self, weekday, start_hour, room_id):
        pass

    def make_booking(self, weekday, start_hour, room_id, course):
        pass

    def delete_booking(self, weekday, start_hour, room_id):
        pass


class Room:
    def __init__(self, id, capacity, campus, calendar, availability=RoomAvailability.Available):
        self.id = id
        self.capacity = capacity
        self.campus = campus
        self.availability = availability
        self.calendar = calendar

    def get_id(self):
        return self.id

    def book_room(self):
        self.availability = RoomAvailability.Busy

    def get_capacity(self):
        pass

    def get_calendar(self):
        pass


class Course:
    def __init__(self, id, education, teacher, student, room):
        self.id = id
        self.education = education
        self.teacher = teacher
        self.student = student
        self.room = room


class Student:
    def __init__(self, id, name, education, course, calendar):
        self.id = id
        self.name = name
        self.education = education
        self.course = course
        self.calendar = calendar


if __name__ == "__main__":
    r = Room("1234", 42, "SUND", Weekday.Monday)
    print(r.availability)
    if r.availability == RoomAvailability.Available:
        r.book_room()
    print(r.availability)