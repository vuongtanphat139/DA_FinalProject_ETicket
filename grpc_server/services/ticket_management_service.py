import grpc
from concurrent import futures
from proto_generate import ticket_management_pb2
from proto_generate import ticket_management_pb2_grpc
import mysql.connector

# Cấu hình kết nối MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="tickets"
)
cursor = db.cursor(dictionary=True)

class TicketService(ticket_management_pb2_grpc.TicketServiceServicer):

    def AddTicket(self, request, context):
        # Thực hiện chèn dữ liệu vào cơ sở dữ liệu MySQL
        query = "INSERT INTO tickets (event_id, ticket_type, ticket_price, total_quantity, available_quantity) VALUES (%s, %s, %s, %s, %s)"
        values = (request.event_id, request.ticket_type, request.ticket_price, request.total_quantity, request.available_quantity)
        cursor.execute(query, values)
        db.commit()  # Commit thay đổi vào cơ sở dữ liệu

        ticket_id = cursor.lastrowid  # Lấy id của ticket vừa thêm vào

        ticket = ticket_management_pb2.Ticket(
            ticket_id=ticket_id,
            event_id=request.event_id,
            ticket_type=request.ticket_type,
            ticket_price=request.ticket_price,
            total_quantity=request.total_quantity,
            available_quantity=request.available_quantity,
        )
        return ticket_management_pb2.TicketResponse(ticket=ticket)

    def UpdateTicket(self, request, context):
        # Thực hiện cập nhật dữ liệu vào cơ sở dữ liệu MySQL
        query = "UPDATE tickets SET event_id=%s, ticket_type=%s, ticket_price=%s, total_quantity=%s, available_quantity=%s WHERE ticket_id=%s"
        values = (request.event_id, request.ticket_type, request.ticket_price, request.total_quantity, request.available_quantity, request.ticket_id)
        cursor.execute(query, values)
        db.commit()  # Commit thay đổi vào cơ sở dữ liệu

        # Kiểm tra xem có ticket nào được cập nhật không
        if cursor.rowcount > 0:
            return ticket_management_pb2.TicketResponse(ticket=request)
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Ticket not found")
            return ticket_management_pb2.TicketResponse()

    def GetAllTickets(self, request, context):
        # Truy vấn tất cả các ticket từ cơ sở dữ liệu MySQL
        query = "SELECT * FROM tickets"
        cursor.execute(query)
        tickets = []
        for row in cursor.fetchall():
            ticket = ticket_management_pb2.Ticket(
                ticket_id=row['ticket_id'],
                event_id=row['event_id'],
                ticket_type=row['ticket_type'],
                ticket_price=row['ticket_price'],
                total_quantity=row['total_quantity'],
                available_quantity=row['available_quantity'],
            )
            tickets.append(ticket)
        return ticket_management_pb2.GetAllTicketsResponse(tickets=tickets)

    def DeleteTicket(self, request, context):
        # Thực hiện xóa ticket khỏi cơ sở dữ liệu MySQL
        query = "DELETE FROM tickets WHERE ticket_id=%s"
        values = (request.ticket_id,)
        cursor.execute(query, values)
        db.commit()  # Commit thay đổi vào cơ sở dữ liệu

        # Kiểm tra xem có ticket nào được xóa không
        if cursor.rowcount > 0:
            return ticket_management_pb2.DeleteTicketResponse(success=True)
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Ticket not found")
            return ticket_management_pb2.DeleteTicketResponse(success=False)
