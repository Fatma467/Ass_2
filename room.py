# room.py
class Room:
    """Represents a room in the hotel."""

    def __init__(self, room_number: int, room_type: str, amenities: list, price_per_night: float, availability: bool):#Initializes a room with number, type, amenities, price, and availability
        self.__room_number = room_number  # Private room number
        self.__room_type = room_type  # Private room type (e.g., Single, Double)
        self.__amenities = amenities  # Private list of amenities
        self.__price_per_night = price_per_night  # Private price per night
        self.__availability = availability  # Private availability status (True/False)

    def check_availability(self):#Returns whether the room is available
        return self.__availability

    def update_availability(self, status: bool):#Updates the availability of the room.
        self.__availability = status

    def __str__(self): #Returns a string representation of the room details
        return f"Room {self.__room_number}: {self.__room_type}, Price: ${self.__price_per_night}, Available: {self.__availability}"

