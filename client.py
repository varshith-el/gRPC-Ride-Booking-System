import logging
import grpc

from protos import ride_service_pb2
from protos import ride_service_pb2_grpc
from protos import driver_service_pb2
from protos import driver_service_pb2_grpc
from protos import user_service_pb2
from protos import user_service_pb2_grpc

class RideHailingClient:
    def __init__(self):
        self.ride_service_client = ride_service_pb2_grpc.RideServiceStub(grpc.insecure_channel('localhost:50051'))
        self.driver_service_client = driver_service_pb2_grpc.DriverServiceStub(grpc.insecure_channel('localhost:50052'))
        self.user_service_client = user_service_pb2_grpc.UserServiceStub(grpc.insecure_channel('localhost:50053'))

    def request_ride(self, user_id, pickup_location, dropoff_location):
        # Get an available driver
        driver_id = self.driver_service_client.GetAvailableDriver(driver_service_pb2.GetAvailableDriverRequest()).driver_id

        # Get the user's information
        user_info = self.user_service_client.GetUser(user_service_pb2.GetUserRequest(user_id=user_id)).user_info

        # Create a new ride request
        ride_request = ride_service_pb2.CreateRideRequest(
            user_id=user_id,
            pickup_location=pickup_location,
            dropoff_location=dropoff_location,
            driver_id=driver_id
        )

        # Call the Ride Service to create a new ride
        ride_response = self.ride_service_client.CreateRide(ride_request)

        return ride_response.ride

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    client = RideHailingClient()
    ride = client.request_ride("user123", "New York", "Los Angeles")
    print(ride)