import logging
import grpc

from protos import ride_service_pb2
from protos import ride_service_pb2_grpc

class RideServiceClient:
    def __init__(self):
        channel = grpc.insecure_channel('localhost:50051')
        self.stub = ride_service_pb2_grpc.RideServiceStub(channel)

    def create_ride(self, pickup_location, dropoff_location, passenger_count):
        request = ride_service_pb2.CreateRideRequest(pickup_location=pickup_location, dropoff_location=dropoff_location, passenger_count=passenger_count)
        response = self.stub.CreateRide(request)
        logging.info("Ride response: %s", response)
        return response

    def get_ride(self, ride_id):
        request = ride_service_pb2.GetRideRequest(ride_id=ride_id)
        response = self.stub.GetRide(request)
        logging.info("Ride response: %s", response)
        return response

    def update_ride(self, ride_id):
        request = ride_service_pb2.UpdateRideRequest(ride_id=ride_id)
        response = self.stub.UpdateRide(request)
        logging.info("Ride response: %s", response)
        return response

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    client = RideServiceClient()
    client.create_ride("New York", "Los Angeles", 2)
    client.get_ride("123")
    client.update_ride("123")