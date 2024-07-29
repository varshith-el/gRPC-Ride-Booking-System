import logging
import grpc

from protos import user_service_pb2
from protos import user_service_pb2_grpc

class UserServiceClient:
    def __init__(self):
        channel = grpc.insecure_channel('localhost:50053')
        self.stub = user_service_pb2_grpc.UserServiceStub(channel)

    def register_user(self, name, email, phone_number, password):
        request = user_service_pb2.RegisterUserRequest(name=name, email=email, phone_number=phone_number, password=password)
        response = self.stub.RegisterUser(request)
        logging.info("User response: %s", response)
        return response

    def login_user(self, user_id, password):
        request = user_service_pb2.LoginUserRequest(user_id=user_id, password=password)
        response = self.stub.LoginUser(request)
        logging.info("User login response: %s", response)
        return response

    def get_user(self, user_id):
        request = user_service_pb2.GetUserRequest(user_id=user_id)
        response = self.stub.GetUser(request)
        logging.info("User response: %s", response)
        return response

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    client = UserServiceClient()
    client.register_user("John Doe", "john@example.com", "1234567890", "password")
    client.login_user("123", "password")
    client.get_user("123")