from room import Room

class Hotel:
    """Represents the hotel that manages rooms and bookings."""

    def __init__(self, name: str, location: str):
        """Initializes a hotel with rooms and bookings."""
        self.__name = name  # Private attribute for hotel name
        self.__location = location  # Private attribute for location
        self.__rooms = []  # Private list of Room objects (Composition: Rooms belong to the hotel)
        self.__bookings = []  # Private list of Booking objects

    def add_room(self, room_number: int, room_type: str, amenities: list, price_per_night: float, availability: bool):
        """
        Adds a room to the hotel's list of rooms by creating it internally.
        This ensures composition, as the hotel owns the rooms.
        """
        room = Room(room_number, room_type, amenities, price_per_night, availability)
        self.__rooms.append(room)

    def create_booking(self, booking):
        """Creates and stores a booking within the hotel."""
        self.__bookings.append(booking)  # Composition: Booking is stored inside the hotel

    def get_bookings(self):
        """Returns all bookings in the hotel."""
        return self.__bookings

    def __str__(self):
        return f"Hotel: {self.__name}, Location: {self.__location}, Bookings: {len(self.__bookings)}"

