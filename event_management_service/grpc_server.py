import grpc
from concurrent import futures
import time
import event_management_pb2
import event_management_pb2_grpc
import mysql.connector

class EventManagementServicer(event_management_pb2_grpc.EventManagementServicer):
    def __init__(self):
        # Cấu hình kết nối MySQL
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123",
            database="event_management"
        )
        self.cursor = self.db.cursor(dictionary=True)
    
    def CreateEvent(self, request, context):
        try:
            # Chèn dữ liệu vào cơ sở dữ liệu
            query = "INSERT INTO Events (name, description, location, datetime) VALUES (%s, %s, %s, %s)"
            values = (request.name, request.description, request.location, request.datetime)
            self.cursor.execute(query, values)
            self.db.commit()
            
            # Lấy ID của sự kiện vừa chèn
            event_id = self.cursor.lastrowid
            
            # Tạo đối tượng Event để trả về
            event = event_management_pb2.Event(
                id=event_id,
                name=request.name,
                description=request.description,
                location=request.location,
                datetime=request.datetime
            )
            
            return event_management_pb2.EventResponse(success=True, message="Event created", event=event)
        except Exception as e:
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INTERNAL)
            return event_management_pb2.EventResponse(success=False, message="Failed to create event")

    def UpdateEvent(self, request, context):
        try:
            # Cập nhật dữ liệu trong cơ sở dữ liệu
            query = "UPDATE Events SET name=%s, description=%s, location=%s, datetime=%s WHERE id=%s"
            values = (request.name, request.description, request.location, request.datetime, request.id)
            self.cursor.execute(query, values)
            self.db.commit()
            
            # Tạo đối tượng Event để trả về
            event = event_management_pb2.Event(
                id=request.id,
                name=request.name,
                description=request.description,
                location=request.location,
                datetime=request.datetime
            )
            
            return event_management_pb2.EventResponse(success=True, message="Event updated", event=event)
        except Exception as e:
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INTERNAL)
            return event_management_pb2.EventResponse(success=False, message="Failed to update event")

    def GetEvent(self, request, context):
        try:
            sql = "SELECT * FROM Events"
            self.cursor.execute(sql)
            events = self.cursor.fetchall()
            event_list = []
            for event in events:
                datetime_str = event['datetime'].strftime('%Y-%m-%dT%H:%M:%S') if event['datetime'] else None
                event_list.append(event_management_pb2.Event(
                    id=event['id'],
                    name=event['name'],
                    description=event['description'],
                    location=event['location'],
                    datetime=datetime_str
                ))
            return event_management_pb2.EventList(events=event_list)
        except Exception as e:
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INTERNAL)
            return event_management_pb2.EventList()

    def SearchEvents(self, request, context):
        try:
            sql = "SELECT * FROM Events WHERE TRUE"
            values = []
            if request.date:
                sql += " AND DATE(datetime) = %s"
                values.append(request.date)
            if request.location:
                sql += " AND location = %s"
                values.append(request.location)
            if request.topic:
                sql += " AND name LIKE %s"
                values.append(f"%{request.topic}%")

            self.cursor.execute(sql, values)
            events = self.cursor.fetchall()
            event_list = []
            for event in events:
                datetime_str = event['datetime'].strftime('%Y-%m-%dT%H:%M:%S') if event['datetime'] else None
                event_list.append(event_management_pb2.Event(
                    id=event['id'],
                    name=event['name'],
                    description=event['description'],
                    location=event['location'],
                    datetime=datetime_str
                ))
            return event_management_pb2.EventList(events=event_list)
        except Exception as e:
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INTERNAL)
            return event_management_pb2.EventList()

    def PurchaseTicket(self, request, context):
        try:
            sql = "INSERT INTO tickets (event_id, user_id, quantity) VALUES (%s, %s, %s)"
            values = (request.event_id, request.user_id, request.quantity)
            self.cursor.execute(sql, values)
            self.db.commit()
            return event_management_pb2.TicketResponse(success=True, message="Ticket purchased")
        except Exception as e:
            return event_management_pb2.TicketResponse(success=False, message=str(e))

    def GetUserEvents(self, request, context):
        try:
            sql = """
                SELECT e.* FROM events e
                JOIN tickets t ON e.id = t.event_id
                WHERE t.user_id = %s
            """
            self.cursor.execute(sql, (request.id,))
            events = self.cursor.fetchall()
            event_list = []
            for event in events:
                datetime_str = event['datetime'].strftime('%Y-%m-%dT%H:%M:%S') if event['datetime'] else None
                event_list.append(event_management_pb2.Event(
                    id=event['id'],
                    name=event['name'],
                    description=event['description'],
                    location=event['location'],
                    datetime=datetime_str
                ))
            return event_management_pb2.EventList(events=event_list)
        except Exception as e:
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INTERNAL)
            return event_management_pb2.EventList()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    event_management_pb2_grpc.add_EventManagementServicer_to_server(EventManagementServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC server is running on port 50051...")
    try:
        while True:
            time.sleep(86400)  # Sleep for one day
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
