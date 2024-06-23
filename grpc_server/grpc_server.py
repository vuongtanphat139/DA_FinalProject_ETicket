import grpc
from concurrent import futures
from proto_generate import ticket_management_pb2_grpc
from services.ticket_management_service import TicketService, OrderService  # Import service từ file ticket_service

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ticket_management_pb2_grpc.add_TicketServiceServicer_to_server(TicketService(), server)
    ticket_management_pb2_grpc.add_OrderServiceServicer_to_server(OrderService(), server)

    server.add_insecure_port("[::]:50052")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()

