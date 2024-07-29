import logging
from concurrent import futures

import grpc

from protos import ride_service_pb2
from protos import ride_service_pb2_grpc

class RideService(ride_service_pb2_grpc.RideServiceServicer):
    def CreateRide(self, request, context):
        # Create a new ride
        ride_id = "123"
        logging.info("Ride created: %s", ride_id)
        return ride_service_pb2.RideResponse(ride_id=ride_id)

    def GetRide(self, request, context):
        # Get a ride by ID
        ride_id = request.ride_id
        logging.info("Ride requested: %s", ride_id)
        ride = ride_service_pb2.RideResponse(
            ride_id=ride_id,
            pickup_location="New York",
            dropoff_location="Los Angeles",
            passenger_count=2,
            driver_id="456",
            vehicle_id="789"
        )
        return ride

    def UpdateRide(self, request, context):
        # Update a ride
        ride_id = request.ride_id
        logging.info("Ride updated: %s", ride_id)
        return ride_service_pb2.RideResponse(ride_id=ride_id)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ride_service_pb2_grpc.add_RideServiceServicer_to_server(RideService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    logging.info("Ride Service server started")
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    serve()