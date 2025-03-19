class Hotel:
    """Represents the hotel that manages rooms and bookings."""

    def __init__(self, name: str, location: str):
        self.__name = name  # Private attribute for hotel name
        self.__location = location  # Private attribute for location
        self.__rooms = []  # Private list of Room objects (Composition: Rooms belong to the hotel)
        self.__bookings = []  # Private list of Booking objects

    def add_room(self, room_number: int, room_type: str, amenities: list, price_per_night: float, availability: bool): #Adds a room to the hotel's list of rooms by creating it internally.
        #This ensures composition, as the hotel owns the rooms.
        room = Room(room_number, room_type, amenities, price_per_night, availability)
        self.__rooms.append(room)

    def create_booking(self, booking): # Creates and stores a booking within the hotel.
        self.__bookings.append(booking)  # Composition: Booking is stored inside the hotel

    def get_bookings(self): #Returns all bookings in the hotel
        return self.__bookings

    def __str__(self):
        return f"Hotel: {self.__name}, Location: {self.__location}, Bookings: {len(self.__bookings)}"
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

# payment.py
class Payment:
    """Represents a payment transaction for a booking."""

    def __init__(self, payment_id: int, booking, amount: float, payment_method: str, status: str = "Pending"): #Initializes a payment with ID, booking, amount, method, and status
        self.__payment_id = payment_id  # Private payment ID
        self.__booking = booking  # Private associated booking
        self.__amount = amount  # Private total amount
        self.__payment_method = payment_method  # Private payment method (e.g., Credit Card)
        self.__status = status  # Private payment status (default = Pending)

    def process_payment(self): #Processes the payment if it is still pending
        if self.__status.lower() == "pending":
            self.__status = "Completed"

    def generate_invoice(self): #Generates an invoice for the payment
        return f"Invoice: Payment {self.__payment_id} | Booking {self.__booking} | Amount: ${self.__amount}"

    def __str__(self): #Returns a string representation of the payment details.
        return f"Payment {self.__payment_id}: ${self.__amount}, Method: {self.__payment_method}, Status: {self.__status}"

# service_request.py
class ServiceRequest:
    """Represents a guest's service request."""

    def __init__(self, request_id: int, guest_id: int, service_type: str, status: str = "Pending"): #Initializes a service request with ID, guest ID, service type, and status
        self.__request_id = request_id  # Private request ID
        self.__guest_id = guest_id  # Private guest ID
        self.__service_type = service_type  # Private service type (e.g., Housekeeping)
        self.__status = status  # Private request status (default = Pending)

    def request_service(self): #Marks the service as requested
        self.__status = "Requested"

    def update_request_status(self, new_status: str): #Updates the status of a service request
        self.__status = new_status

    def __str__(self): #Returns a string representation of the service request details
        return f"ServiceRequest {self.__request_id}: Guest {self.__guest_id}, Service: {self.__service_type}, Status: {self.__status}"

# Running the system
if __name__ == "__main__":
    # Create a hotel
    hotel = Hotel("The Address", "Downtown")

    # Add rooms to the hotel (internally created by the hotel)
    hotel.add_room(101, "Single", ["WiFi", "TV"], 100.0, True)
    hotel.add_room(102, "Double", ["WiFi", "TV", "Mini-bar"], 150.0, True)

    # Create a guest
    guest1 = Guest(1, "Fatma", "fatma@gmail.com")

    # Get the first room from the hotel's internal list of rooms
    room1 = hotel._Hotel__rooms[0]  # Accessing private attribute for demonstration purposes

    # Create a booking
    booking1 = Booking(1, guest1, room1, "2025-04-01", "2025-04-05")
    booking1.confirm_booking()

    # Create a payment
    payment1 = Payment(1, booking1, 400.0, "Credit Card")
    payment1.process_payment()

    # Create a service request
    service_request1 = ServiceRequest(1, guest1, "Housekeeping")
    service_request1.request_service()

    # Display results
    print(hotel)
    print(booking1)
    print(payment1)
    print(service_request1)