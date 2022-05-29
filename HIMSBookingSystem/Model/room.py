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
