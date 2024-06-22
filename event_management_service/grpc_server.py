import grpc
from concurrent import futures
import time
import event_management_pb2
import event_management_pb2_grpc
import mysql.connector

class EventManagementServicer(event_management_pb2_grpc.EventManagementServicer):
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123",
            database="event_management"
        )
        self.cursor = self.db.cursor(dictionary=True)

    def CreateEvent(self, request, context):
        try:
            # Xử lý request từ client, ví dụ như lưu vào cơ sở dữ liệu
            # Sau khi lưu thành công, trả về thông báo thành công và thông tin sự kiện đã tạo
            return event_management_pb2.EventResponse(
                success=True,
                message="Event created successfully.",
                event=event_management_pb2.Event(
                    id=1,  # Thay bằng id của sự kiện đã tạo
                    name=request.name,
                    description=request.description,
                    location=request.location,
                    datetime=request.datetime,
                    bannerURL=request.bannerURL,
                    url=request.url,
                    venue=request.venue,
                    address=request.address,
                    orgId=request.orgId,
                    minTicketPrice=request.minTicketPrice,
                    status=request.status,
                    statusName=request.statusName,
                    orgLogoURL=request.orgLogoURL,
                    orgName=request.orgName,
                    orgDescription=request.orgDescription,
                    categories=request.categories
                )
            )
        except Exception as e:
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INTERNAL)
            return event_management_pb2.EventResponse(success=False, message="Failed to create event.")
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INTERNAL)
            return event_management_pb2.EventResponse(success=False, message="Failed to create event")

    def UpdateEvent(self, request, context):
        try:
            # Xử lý request từ client, ví dụ như cập nhật vào cơ sở dữ liệu
            # Sau khi cập nhật thành công, trả về thông báo thành công và thông tin sự kiện đã cập nhật
            return event_management_pb2.EventResponse(
                success=True,
                message="Event updated successfully.",
                event=event_management_pb2.Event(
                    id=request.id,
                    name=request.name,
                    description=request.description,
                    location=request.location,
                    datetime=request.datetime,
                    bannerURL=request.bannerURL,
                    url=request.url,
                    venue=request.venue,
                    address=request.address,
                    orgId=request.orgId,
                    minTicketPrice=request.minTicketPrice,
                    status=request.status,
                    statusName=request.statusName,
                    orgLogoURL=request.orgLogoURL,
                    orgName=request.orgName,
                    orgDescription=request.orgDescription,
                    categories=request.categories
                )
            )
        except Exception as e:
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INTERNAL)
            return event_management_pb2.EventResponse(success=False, message="Failed to update event.")

    def GetEvent(self, request, context):
        try:
            sql = "SELECT * FROM Events"
            self.cursor.execute(sql)
            events = self.cursor.fetchall()
            event_list = []
            for event in events:
                event_list.append(event_management_pb2.Event(
                    id=int(event['id']),
                    name=event['name'],
                    description=event['description'],
                    location=event['location'],
                    datetime=event['datetime'].strftime("%Y-%m-%d %H:%M:%S"),  # Chuyển đổi thành string theo định dạng mong muốn
                    bannerURL=event['bannerURL'],
                    url=event['url'],
                    venue=event['venue'],
                    address=event['address'],
                    orgId=int(event['orgId']),
                    minTicketPrice=int(event['minTicketPrice']),
                    status=event['status'],
                    statusName=event['statusName'],
                    orgLogoURL=event['orgLogoURL'],
                    orgName=event['orgName'],
                    orgDescription=event['orgDescription'],
                    categories=event['categories']
                ))
            return event_management_pb2.EventList(events=event_list)
        except Exception as e:
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INTERNAL)
            return event_management_pb2.EventList()

    def SearchEvents(self, request, context):
        try:
            # Xử lý request từ client, ví dụ như truy vấn cơ sở dữ liệu và lấy danh sách sự kiện thỏa mãn các điều kiện tìm kiếm
            # Trả về danh sách các sự kiện tìm được
            events = [
                event_management_pb2.Event(
                    id=1,  # Thay bằng id của từng sự kiện
                    name="Example Event",
                    description="Example description",
                    location="Example location",
                    datetime="2024-06-30 18:00:00",  # Thay bằng định dạng datetime thực tế
                    bannerURL="http://example.com/banner.jpg",
                    url="http://example.com",
                    venue="Example venue",
                    address="Example address",
                    orgId=1,  # Thay bằng id của tổ chức
                    minTicketPrice=100000,  # Thay bằng giá vé tối thiểu
                    status="active",
                    statusName="Active",
                    orgLogoURL="http://example.com/logo.jpg",
                    orgName="Example Organization",
                    orgDescription="Example organization description",
                    categories="Music, Concert"
                )
            ]
            return event_management_pb2.EventList(events=events)
        except Exception as e:
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INTERNAL)
            return event_management_pb2.EventList()

    def PurchaseTicket(self, request, context):
        try:
            # Xử lý yêu cầu mua vé từ client
            # Sau khi xử lý thành công, trả về thông báo thành công
            return event_management_pb2.TicketResponse(
                success=True,
                message="Ticket purchased successfully."
            )
        except Exception as e:
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INTERNAL)
            return event_management_pb2.TicketResponse(success=False, message="Failed to purchase ticket.")

    def GetUserEvents(self, request, context):
        try:
            # Xử lý yêu cầu lấy danh sách sự kiện của người dùng từ client
            # Trả về danh sách các sự kiện của người dùng
            events = [
                event_management_pb2.Event(
                    id=1,  # Thay bằng id của từng sự kiện
                    name="Example Event",
                    description="Example description",
                    location="Example location",
                    datetime="2024-06-30 18:00:00",  # Thay bằng định dạng datetime thực tế
                    bannerURL="http://example.com/banner.jpg",
                    url="http://example.com",
                    venue="Example venue",
                    address="Example address",
                    orgId=1,  # Thay bằng id của tổ chức
                    minTicketPrice=100000,  # Thay bằng giá vé tối thiểu
                    status="active",
                    statusName="Active",
                    orgLogoURL="http://example.com/logo.jpg",
                    orgName="Example Organization",
                    orgDescription="Example organization description",
                    categories="Music, Concert"
                )
            ]
            return event_management_pb2.EventList(events=events)
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
