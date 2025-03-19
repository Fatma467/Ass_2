from booking import Booking
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
