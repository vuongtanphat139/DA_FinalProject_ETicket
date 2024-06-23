import grpc
from concurrent import futures
from proto_generate import ticket_management_pb2
from proto_generate import ticket_management_pb2_grpc
import mysql.connector

<<<<<<< HEAD
# Cấu hình kết nối MySQL
=======
>>>>>>> origin/ticket_management3
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="tickets"
)
cursor = db.cursor(dictionary=True)

<<<<<<< HEAD
class TicketService(ticket_management_pb2_grpc.TicketServiceServicer):

=======

class TicketService(ticket_management_pb2_grpc.TicketServiceServicer):

    # Cấu hình kết nối MySQL
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="tickets"
    )
    cursor = db.cursor(dictionary=True)

>>>>>>> origin/ticket_management3
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
<<<<<<< HEAD
=======

class OrderService(ticket_management_pb2_grpc.OrderServiceServicer):
    # Cấu hình kết nối MySQL

    def AddOrder(self, request: ticket_management_pb2.OrderRequest, context: grpc.ServicerContext) -> ticket_management_pb2.OrderResponse:
        try:
            # Thêm đơn hàng vào cơ sở dữ liệu
            order_query = "INSERT INTO Orders (customer_name, total_price, status) VALUES (%s, %s, %s)"
            values = (request.customer_name, request.total_price, "pending")
            cursor.execute(order_query, values)
            db.commit()  # Commit thay đổi vào cơ sở dữ liệu
            order_id = cursor.lastrowid  # Lấy id của đơn hàng vừa thêm vào
    
            # Thêm các mục đơn hàng vào cơ sở dữ liệu
            for item in request.items:
                item_query = "INSERT INTO OrderItems (order_id, ticket_id, quantity, price) VALUES (%s, %s, %s, %s)"
                item_values = (order_id, item.ticket_id, item.quantity, item.price)
                cursor.execute(item_query, item_values)
    
            db.commit()  # Commit thay đổi vào cơ sở dữ liệu
    
            order = ticket_management_pb2.Order(
                order_id=order_id,
                customer_name=request.customer_name,
                items=request.items,
                total_price=request.total_price,
                status="pending"  # Đặt giá trị mặc định cho trường status là "pending"
            )
            return ticket_management_pb2.OrderResponse(order=order)
    
        except mysql.connector.Error as err:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"Error adding order: {err}")
            return ticket_management_pb2.OrderResponse()
    

    def UpdateOrder(self, request: ticket_management_pb2.Order, context: grpc.ServicerContext) -> ticket_management_pb2.OrderResponse:
        try:
            # Cập nhật thông tin đơn hàng
            order_query = "UPDATE Orders SET customer_name=%s, total_price=%s, status=%s WHERE order_id=%s"
            order_values = (request.customer_name, request.total_price, request.status, request.order_id)
            cursor.execute(order_query, order_values)

            # Xóa các mục đơn hàng cũ
            delete_items_query = "DELETE FROM OrderItems WHERE order_id=%s"
            cursor.execute(delete_items_query, (request.order_id,))

            # Thêm các mục đơn hàng mới
            for item in request.items:
                item_query = "INSERT INTO OrderItems (order_id, ticket_id, quantity, price) VALUES (%s, %s, %s, %s)"
                item_values = (request.order_id, item.ticket_id, item.quantity, item.price)
                cursor.execute(item_query, item_values)

            db.commit()  # Commit thay đổi vào cơ sở dữ liệu

            return ticket_management_pb2.OrderResponse(order=request)

        except mysql.connector.Error as err:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"Error updating order: {err}")
            return ticket_management_pb2.OrderResponse()

    def GetAllOrders(self, request: ticket_management_pb2.GetAllOrdersRequest, context: grpc.ServicerContext) -> ticket_management_pb2.GetAllOrdersResponse:
        try:
            # Truy vấn tất cả các order từ cơ sở dữ liệu MySQL
            query = "SELECT * FROM Orders"
            cursor.execute(query)
            orders = []

            for row in cursor.fetchall():
                # Truy vấn các mục đơn hàng tương ứng
                item_query = "SELECT * FROM OrderItems WHERE order_id=%s"
                cursor.execute(item_query, (row['order_id'],))
                items = [ticket_management_pb2.OrderItem(ticket_id=item['ticket_id'], quantity=item['quantity'], price=item['price']) for item in cursor.fetchall()]

                order = ticket_management_pb2.Order(
                    order_id=row['order_id'],
                    customer_name=row['customer_name'],
                    items=items,
                    total_price=row['total_price'],
                    status=row['status']
                )
                orders.append(order)

            return ticket_management_pb2.GetAllOrdersResponse(orders=orders)

        except mysql.connector.Error as err:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"Error fetching orders: {err}")
            return ticket_management_pb2.GetAllOrdersResponse()

    def DeleteOrder(self, request: ticket_management_pb2.DeleteOrderRequest, context: grpc.ServicerContext) -> ticket_management_pb2.DeleteOrderResponse:
        try:
            # Thực hiện xóa order khỏi cơ sở dữ liệu MySQL
            query = "DELETE FROM Orders WHERE order_id=%s"
            values = (request.order_id,)
            cursor.execute(query, values)
            db.commit()  # Commit thay đổi vào cơ sở dữ liệu

            # Kiểm tra xem có order nào được xóa không
            if cursor.rowcount > 0:
                return ticket_management_pb2.DeleteOrderResponse(success=True)
            else:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details("Order not found")
                return ticket_management_pb2.DeleteOrderResponse(success=False)

        except mysql.connector.Error as err:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"Error deleting order: {err}")
            return ticket_management_pb2.DeleteOrderResponse(success=False)
>>>>>>> origin/ticket_management3
