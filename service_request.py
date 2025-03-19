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
