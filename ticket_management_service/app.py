import grpc
from concurrent import futures
import ticket_management_pb2
import ticket_management_pb2_grpc
import mysql.connector
import time

try:
    db = mysql.connector.connect(
        # host='mysql-db',
        user='root',
        password='123',
        database='ticket_management',
        port=3308
    )
    cursor = db.cursor(dictionary=True)
    print("Connected to the database successfully.")
except mysql.connector.Error as err:
    print(f"Error: {err}")
    db = None
    cursor = None

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
    
    def GetAllTicketsByEvent(self, request, context):
        # Truy vấn tất cả các tickets theo event id từ cơ sở dữ liệu MySQL

        query = "SELECT * FROM tickets WHERE event_id = %s"
        cursor.execute(query, (request.event_id,))
        tickets = []
        print("Request event_id:", request.event_id)  
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
        return ticket_management_pb2.GetAllTicketsByEventResponse(tickets=tickets)

    def GetTicketById(self, request, context):
        # Truy vấn một ticket từ cơ sở dữ liệu MySQL dựa trên ticket_id
        query = "SELECT * FROM tickets WHERE ticket_id = %s"
        cursor.execute(query, (request.ticket_id,))
        row = cursor.fetchone()
        if row:
            ticket = ticket_management_pb2.Ticket(
                ticket_id=row['ticket_id'],
                event_id=row['event_id'],
                ticket_type=row['ticket_type'],
                ticket_price=row['ticket_price'],
                total_quantity=row['total_quantity'],
                available_quantity=row['available_quantity'],
            )
            return ticket_management_pb2.GetTicketByIdResponse(ticket=ticket)
        else:
            context.set_details('Ticket not found')
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return ticket_management_pb2.GetTicketByIdResponse()


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

class OrderService(ticket_management_pb2_grpc.OrderServiceServicer):
    def GetAllOrders(self, request: ticket_management_pb2.GetAllOrdersRequest, context: grpc.ServicerContext) -> ticket_management_pb2.GetAllOrdersResponse:
        try:
            print("Fetching all orders...")  # Thêm nhật ký
    
            # Tạo con trỏ để truy vấn Orders
            cursor = db.cursor(dictionary=True)
    
            # Truy vấn tất cả các đơn hàng từ cơ sở dữ liệu MySQL
            query = "SELECT * FROM Orders"
            cursor.execute(query)
            orders = []
    
            for row in cursor.fetchall():
                print(f"Order found: {row['order_id']}")  # Thêm nhật ký
    
                # Tạo con trỏ mới cho mỗi truy vấn mục đơn hàng
                items_cursor = db.cursor(dictionary=True)
    
                # Truy vấn các mục đơn hàng tương ứng với mỗi order_id
                item_query = "SELECT * FROM OrderItems WHERE order_id=%s"
                items_cursor.execute(item_query, (row['order_id'],))
                items = [ticket_management_pb2.OrderItem(
                            order_item_id = item['order_item_id'],
                            ticket_id=item['ticket_id'],
                            quantity=item['quantity'],
                            price=item['price']
                        ) for item in items_cursor.fetchall()]
    
                # Tạo đối tượng Order protobuf từ kết quả truy vấn
                order = ticket_management_pb2.Order(
                    order_id=row['order_id'],
                    customer_name=row['customer_name'],
                    items=items,
                    total_price=row['total_price'],
                    status=row['status']
                )
                orders.append(order)
    
                # Đóng con trỏ sau khi sử dụng
                items_cursor.close()
    
            # Đóng con trỏ sau khi sử dụng
            cursor.close()
    
            print(f"Total orders fetched: {len(orders)}")  # Thêm nhật ký
    
            # Trả về danh sách tất cả các đơn hàng
            return ticket_management_pb2.GetAllOrdersResponse(orders=orders)
    
        except mysql.connector.Error as err:
            # Xử lý lỗi cơ sở dữ liệu
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"Error fetching orders: {err}")
            return ticket_management_pb2.GetAllOrdersResponse()
    


    def GetOrderById(self, request, context):
        try:
            order_id = request.order_id

            # Query to fetch the order details from MySQL
            order_query = "SELECT * FROM Orders WHERE order_id = %s"
            cursor.execute(order_query, (order_id,))
            row = cursor.fetchone()

            if not row:
                # Handle case where order_id does not exist
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details(f"Order with ID {order_id} not found")
                return ticket_management_pb2.OrderResponse()

            # Fetch order items for the given order_id
            item_query = "SELECT * FROM OrderItems WHERE order_id = %s"
            cursor.execute(item_query, (order_id,))
            items = [ticket_management_pb2.OrderItem(
                        order_item_id = item['order_item_id'],
                        ticket_id=item['ticket_id'],
                        quantity=item['quantity'],
                        price=item['price']
                    ) for item in cursor.fetchall()]

            # Construct the gRPC response with order details
            order = ticket_management_pb2.Order(
                order_id=row['order_id'],
                customer_name=row['customer_name'],
                items=items,
                total_price=row['total_price'],
                status=row['status']
            )

            return ticket_management_pb2.OrderResponse(order=order)

        except mysql.connector.Error as err:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"Error fetching order details: {err}")
            return ticket_management_pb2.OrderResponse()


    # def UpdateOrderStatus(self, request, context):
    #     try:
    #         # Update only the 'status' field in the database
    #         order_query = "UPDATE Orders SET status=%s WHERE order_id=%s"
    #         order_values = (request.status, request.order_id)
    #         cursor.execute(order_query, order_values)
    #         db.commit()  

    #         # Fetch the updated order from the database (if needed)
            
    #     except mysql.connector.Error as err:
    #             context.set_code(grpc.StatusCode.INTERNAL)
    #             context.set_details(f"Error updating order status: {err}")
    #             return ticket_management_pb2.OrderResponse()

    # Cấu hình kết nối MySQL

    def AddOrder(self, request, context):
        try:
            # Thêm đơn hàng vào cơ sở dữ liệu
            order_query = "INSERT INTO Orders (customer_name, total_price, status) VALUES (%s, %s, %s)"
            values = (request.customer_name, request.total_price, "pending")
            cursor.execute(order_query, values)
            #db.commit()  # Commit thay đổi vào cơ sở dữ liệu
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
            db.rollback()  # Rollback nếu có lỗi xảy ra
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"Error adding order: {err}")
            return ticket_management_pb2.OrderResponse()
    

    def UpdateOrder(self, request, context):
        try:
            # Cập nhật thông tin đơn hàng
            order_query = "UPDATE Orders SET customer_name=%s, total_price=%s, status=%s WHERE order_id=%s"
            order_values = (request.customer_name, request.total_price, request.status, request.order_id)
            cursor.execute(order_query, order_values)

            # # Xóa các mục đơn hàng cũ
            # delete_items_query = "DELETE FROM OrderItems WHERE order_id=%s"
            # cursor.execute(delete_items_query, (request.order_id,))

            # # Thêm các mục đơn hàng mới
            # for item in request.items:
            #     item_query = "INSERT INTO OrderItems (order_id, ticket_id, quantity, price) VALUES (%s, %s, %s, %s)"
            #     item_values = (request.order_id, item.ticket_id, item.quantity, item.price)
            #     cursor.execute(item_query, item_values)

            db.commit()  # Commit thay đổi vào cơ sở dữ liệu

            return ticket_management_pb2.OrderResponse(order=request)

        except mysql.connector.Error as err:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"Error updating order: {err}")
            return ticket_management_pb2.OrderResponse()


    # def DeleteOrder(self, request: ticket_management_pb2.DeleteOrderRequest, context: grpc.ServicerContext) -> ticket_management_pb2.DeleteOrderResponse:
    #     try:
    #         # Thực hiện xóa order khỏi cơ sở dữ liệu MySQL
    #         query = "DELETE FROM Orders WHERE order_id=%s"
    #         values = (request.order_id,)
    #         cursor.execute(query, values)
    #         db.commit()  # Commit thay đổi vào cơ sở dữ liệu

    #         # Kiểm tra xem có order nào được xóa không
    #         if cursor.rowcount > 0:
    #             return ticket_management_pb2.DeleteOrderResponse(success=True)
    #         else:
    #             context.set_code(grpc.StatusCode.NOT_FOUND)
    #             context.set_details("Order not found")
    #             return ticket_management_pb2.DeleteOrderResponse(success=False)

    #     except mysql.connector.Error as err:
    #         context.set_code(grpc.StatusCode.INTERNAL)
    #         context.set_details(f"Error deleting order: {err}")
    #         return ticket_management_pb2.DeleteOrderResponse(success=False)

    # def UpdateOrderStatus(self, request: ticket_management_pb2.Order, context: grpc.ServicerContext) -> ticket_management_pb2.OrderResponse:
    #     try:
    #         # Update only the 'status' field in the database
    #         order_query = "UPDATE Orders SET status=%s WHERE order_id=%s"
    #         order_values = (request.status, request.order_id)
    #         cursor.execute(order_query, order_values)
    #         db.commit()  # Commit changes to the database

    #         # Fetch the updated order from the database (if needed)

    #     except mysql.connector.Error as err:
    #         context.set_code(grpc.StatusCode.INTERNAL)
    #         context.set_details(f"Error updating order status: {err}")
    #         return ticket_management_pb2.OrderResponse()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ticket_management_pb2_grpc.add_TicketServiceServicer_to_server(TicketService(), server)
    ticket_management_pb2_grpc.add_OrderServiceServicer_to_server(OrderService(), server)
    server.add_insecure_port("[::]:50052")
    server.start()
    print("gRPC server is running on port 50052...")
    try:
        while True:
            time.sleep(86400)  # Sleep for one day
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == "__main__":
    serve()