import unittest  # Import unittest module for creating test cases
from hotel import Hotel  # Import Hotel class from hotel module
from room import Room  # Import Room class from room module
from guest import Guest  # Import Guest class from guest module
from booking import Booking  # Import Booking class from booking module
from payment import Payment  # Import Payment class from payment module
from service_request import ServiceRequest  # Import ServiceRequest class from service_request module


def get_user_input(prompt):  # Define a function to get user input safely
    try:
        return input(prompt)  # Prompt the user for input and return it
    except Exception as e:  # Catch any exceptions that occur
        print(f"Error: {e}")  # Print the error message
        return None  # Return None if an error occurs


class TestHotelSystem(unittest.TestCase):  # Define a test class inheriting from unittest.TestCase
    """Test suite for the hotel management system, covering guest creation, room reservations, and payment processing."""
    def setUp(self):  # Setup method to initialize test data before each test
        self.hotel = Hotel("The Address", "Downtown")  # Create a hotel instance
        self.hotel.add_room(101, "Single", ["WiFi", "TV"], 100.0, True)  # Add a single room to the hotel
        self.hotel.add_room(102, "Double", ["WiFi", "TV", "Mini-bar"], 150.0, True)  # Add a double room to the hotel

    def test_guest_account_creation(self):  # Define a test case for guest account creation
        try:
            guest_id = int(get_user_input("Enter Guest ID: "))  # Get and convert guest ID from user input
            name = get_user_input("Enter Guest Name: ")  # Get guest name from user input
            contact_info = get_user_input("Enter Contact Info: ")  # Get contact information from user input
            guest = Guest(guest_id, name, contact_info)  # Create a Guest object
            self.assertEqual(guest._Guest__name, name)  # Verify guest name is correctly stored
            self.assertEqual(guest._Guest__contact_info, contact_info)  # Verify contact info is correctly stored
        except ValueError:  # Handle incorrect input type
            print("Invalid input! Please enter a valid guest ID.")  # Print error message

    def test_make_room_reservation(self):  # Define a test case for making a room reservation
        try:
            guest_id = int(get_user_input("Enter Guest ID: "))  # Get and convert guest ID from user input
            guest_name = get_user_input("Enter Guest Name: ")  # Get guest name from user input
            guest_email = get_user_input("Enter Guest Email: ")  # Get guest email from user input
            guest = Guest(guest_id, guest_name, guest_email)  # Create a Guest object
            room_choice = int(get_user_input("Enter Room Number (101 or 102): "))  # Get and convert room number
            room = next((r for r in self.hotel._Hotel__rooms if r._Room__room_number == room_choice), None)  # Find the selected room
            if room and room.check_availability():  # Check if the room is available
                booking = Booking(1, guest, room, "2025-04-01", "2025-04-05")  # Create a booking object
                booking.confirm_booking()  # Confirm the booking
                print("Booking confirmed!")  # Print confirmation message
                self.assertEqual(booking._Booking__status, "Confirmed")  # Verify booking status is confirmed
                self.assertFalse(room.check_availability())  # Verify room is no longer available
            else:
                print("Room not available or invalid room number.")  # Print error message if room is unavailable
        except ValueError:  # Handle incorrect input type
            print("Invalid input! Please enter numbers where required.")  # Print error message

    def test_payment_processing(self):  # Define a test case for payment processing
        """Test processing a payment with user input."""
        try:
            payment_id = int(get_user_input("Enter Payment ID: "))  # Get and convert payment ID from user input
            amount = float(get_user_input("Enter Payment Amount: "))  # Get and convert payment amount
            payment_method = get_user_input("Enter Payment Method (Credit Card, Debit Card, Mobile Wallet): ")  # Get payment method
            payment = Payment(payment_id, None, amount, payment_method)  # Create a Payment object
            payment.process_payment()  # Process the payment
            print("Payment processed successfully!")  # Print success message
            self.assertEqual(payment._Payment__status, "Completed")  # Verify payment status is completed
        except ValueError:  # Handle incorrect input type
            print("Invalid input! Please enter numbers where required.")  # Print error message


if __name__ == "__main__":  # Run the tests only if the script is executed directly
    unittest.main()  # Execute all test cases
