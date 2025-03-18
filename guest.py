# guest.py
class Guest:
    """Represents a hotel guest."""

    def __init__(self, guest_id: int, name: str, contact_info: str, loyalty_points: int = 0): #Initializes a guest with ID, name, contact details, and loyalty points
        self.__guest_id = guest_id  # Private guest ID
        self.__name = name  # Private name
        self.__contact_info = contact_info  # Private contact details
        self.__loyalty_points = loyalty_points  # Private loyalty points (default = 0)

    def update_profile(self, new_contact_info): #Updates guest contact information
        self.__contact_info = new_contact_info

    def view_bookings(self, bookings): #Returns a list of bookings associated with this guest
        return [str(booking) for booking in bookings if booking._Booking__guest == self]

    def __str__(self): #Returns a string representation of the guest details
        return f"Guest {self.__guest_id}: {self.__name}, Contact: {self.__contact_info}, Points: {self.__loyalty_points}"
