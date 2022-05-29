class Teacher(Employee):
    def __init__(self, id, firstname, lastname, campus, education, courses, calendar):
        super().__init__(id, firstname, lastname, campus, education)
        self.courses = courses
        self.calendar = Weekday.Monday

    def get_calendar(self):
        return self.calendar

    def book_room(self, booking_manager):
        pass