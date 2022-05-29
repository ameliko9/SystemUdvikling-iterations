# import datatime
# weekdays = ("Monday")
from enum import Enum

class RoomAvailability(Enum):
    Available = 1
    Busy = 0


if __name__ == "__main__":
    r = Room("1234", 42, "SUND", Weekday.Monday)
    print(r.availability)
    if r.availability == RoomAvailability.Available:
        r.book_room()
    print(r.availability)