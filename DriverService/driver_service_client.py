import logging
import grpc

import driver_service_pb2
import driver_service_pb2_grpc

class DriverServiceClient:
    def __init__(self):
        channel = grpc.insecure_channel('localhost:50052')
        self.stub = driver_service_pb2_grpc.DriverServiceStub(channel)

    def register_driver(self, name, email, phone_number):
        request = driver_service_pb2.DriverRegistrationRequest(name=name, email=email, phone_number=phone_number)
        response = self.stub.RegisterDriver(request)
        logging.info("Driver response: %s", response)
        return response

    def update_driver_availability(self, driver_id, availability):
        request = driver_service_pb2.DriverAvailabilityRequest(driver_id=driver_id, available=availability)
        response = self.stub.UpdateDriverAvailability(request)
        logging.info("Driver availability response: %s", response)
        return response

    def get_driver(self, driver_id):
        request = driver_service_pb2.DriverId(driver_id=driver_id)
        response = self.stub.GetDriver(request)
        logging.info("Driver response: %s", response)
        return response

    def assign_driver(self, ride_id):
        # This will not work because AssignDriverRequest and AssignDriverResponse are not defined in the proto file
        # request = driver_service_pb2.AssignDriverRequest(ride_id=ride_id)
        # response = self.stub.AssignDriver(request)
        # logging.info("Assign driver response: %s", response)
        # return response
        pass

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    client = DriverServiceClient()
    client.register_driver("John Doe", "john@example.com", "1234567890")
    client.update_driver_availability("123", True)
    client.get_driver("123")