from room import Room
from guest import Guest

# booking.py
class Booking:
    """Represents a hotel room booking."""

    def __init__(self, booking_id: int, guest, room, check_in_date: str, check_out_date: str, status: str = "Pending"): #Initializes a booking with ID, guest, room, dates, and status
        self.__booking_id = booking_id  # Private booking ID
        self.__guest = guest  # Private guest object
        self.__room = room  # Private room object
        self.__check_in_date = check_in_date  # Private check-in date
        self.__check_out_date = check_out_date  # Private check-out date
        self.__status = status  # Private booking status (default = Pending)

    def confirm_booking(self):#Confirms the booking if the room is available
        if self.__room.check_availability():
            self.__status = "Confirmed"
            self.__room.update_availability(False)
        else:
            self.__status = "Failed - Room Unavailable"

    def cancel_booking(self): #Cancels the booking and marks the room as available again
        self.__status = "Cancelled"
        self.__room.update_availability(True)

    def __str__(self): #Returns a string representation of the booking details
        return f"Booking {self.__booking_id}: Guest {self.__guest}, Room {self.__room}, Status: {self.__status}"
