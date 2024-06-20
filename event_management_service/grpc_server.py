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
        # Ví dụ về việc tạo sự kiện (bạn có thể bổ sung thêm logic thực tế)
        return event_management_pb2.EventResponse(success=True, message="Event created", event=request)
    
    def UpdateEvent(self, request, context):
        # Ví dụ về việc cập nhật sự kiện (bạn có thể bổ sung thêm logic thực tế)
        return event_management_pb2.EventResponse(success=True, message="Event updated", event=request)
    
    def GetEvent(self, request, context):
        # Truy vấn cơ sở dữ liệu để lấy tất cả các sự kiện
        self.cursor.execute("SELECT * FROM Events")
        events = self.cursor.fetchall()
        event_list = []
        for event in events:
            # Chuyển đổi datetime từ cơ sở dữ liệu thành chuỗi
            datetime_str = event['datetime'].strftime('%Y-%m-%dT%H:%M:%S') if event['datetime'] else None
            event_list.append(event_management_pb2.Event(
                id=event['id'],
                name=event['name'],
                description=event['description'],
                location=event['location'],
                datetime=datetime_str
            ))
        return event_management_pb2.EventList(events=event_list)
    
    def SearchEvents(self, request, context):
        # Ví dụ về tìm kiếm sự kiện (bạn có thể bổ sung thêm logic thực tế)
        events = [
            event_management_pb2.Event(id=1, name="Event 1", description="Description 1", location="Location 1", datetime="2024-06-20T12:00:00"),
            event_management_pb2.Event(id=2, name="Event 2", description="Description 2", location="Location 2", datetime="2024-06-21T14:00:00")
        ]
        return event_management_pb2.EventList(events=events)
    
    def PurchaseTicket(self, request, context):
        # Ví dụ về việc mua vé (bạn có thể bổ sung thêm logic thực tế)
        return event_management_pb2.TicketResponse(success=True, message="Ticket purchased")
    
    def GetUserEvents(self, request, context):
        # Ví dụ về việc lấy sự kiện của người dùng (bạn có thể bổ sung thêm logic thực tế)
        events = [
            event_management_pb2.Event(id=1, name="Event 1", description="Description 1", location="Location 1", datetime="2024-06-20T12:00:00")
        ]
        return event_management_pb2.EventList(events=events)

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
