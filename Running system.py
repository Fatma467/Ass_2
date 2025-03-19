# main.py - Running the system
if __name__ == "__main__":
    # Create a hotel
    hotel = Hotel("The Address", "Downtown")

    # Add rooms to the hotel (internally created by the hotel)
    hotel.add_room(101, "Single", ["WiFi", "TV"], 100.0, True)
    hotel.add_room(102, "Double", ["WiFi", "TV", "Mini-bar"], 150.0, True)

    # Create a guest
    guest1 = Guest(1, "Alice", "alice@gmail.com")

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