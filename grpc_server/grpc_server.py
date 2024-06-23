import grpc
from concurrent import futures
from proto_generate import ticket_management_pb2_grpc
from services.ticket_management_service import TicketService  # Import service từ file ticket_service

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ticket_management_pb2_grpc.add_TicketServiceServicer_to_server(TicketService(), server)
    server.add_insecure_port("[::]:50053")  # use a different port from previous example
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
