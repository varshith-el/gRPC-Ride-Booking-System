import logging
from concurrent import futures

import grpc

from protos import user_service_pb2
from protos import user_service_pb2_grpc

class UserService(user_service_pb2_grpc.UserServiceServicer):
    def RegisterUser(self, request, context):
        # Register a new user
        user_id = "123"
        logging.info("User registered: %s", user_id)
        return user_service_pb2.RegisterUserResponse(user_id=user_id)

    def LoginUser(self, request, context):
        # Login a user
        user_id = request.user_id
        password = request.password
        logging.info("User logged in: %s %s", user_id, password)
        return user_service_pb2.LoginUserResponse()

    def GetUser(self, request, context):
        # Get a user by ID
        user_id = request.user_id
        logging.info("User requested: %s", user_id)
        user = user_service_pb2.UserResponse(
            user_id=user_id,
            name="John Doe",
            email="john@example.com",
            phone_number="1234567890"
        )
        return user

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_service_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
    server.add_insecure_port('[::]:50053')
    server.start()
    logging.info("User Service server started")
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    serve()