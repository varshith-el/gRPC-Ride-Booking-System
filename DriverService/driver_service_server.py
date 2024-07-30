import logging
from concurrent import futures

import grpc

import driver_service_pb2
import driver_service_pb2_grpc

class DriverService(driver_service_pb2_grpc.DriverServiceServicer):
    def RegisterDriver(self, request, context):
        # Register a new driver
        driver_id = "123"
        logging.info("Driver registered: %s", driver_id)
        return driver_service_pb2.DriverRegistrationResponse(driver_id=driver_id)

    def UpdateDriverAvailability(self, request, context):
        # Update a driver's availability
        driver_id = request.driver_id
        availability = request.available
        logging.info("Driver availability updated: %s %s", driver_id, availability)
        return driver_service_pb2.DriverAvailabilityResponse(driver_id=driver_id, available=availability)

    def GetDriver(self, request, context):
        # Get a driver by ID
        driver_id = request.driver_id
        logging.info("Driver requested: %s", driver_id)
        driver = driver_service_pb2.DriverResponse(
            driver_id=driver_id,
            name="John Doe",
            email="john@example.com",
            phone_number="1234567890",
            vehicle_type="Sedan",
            vehicle_registration_number="ABC123"
        )
        return driver

    def AssignDriver(self, request, context):
        pass

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    driver_service_pb2_grpc.add_DriverServiceServicer_to_server(DriverService(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    logging.info("Driver Service server started")
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    serve()