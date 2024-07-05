from flask import Flask
from flask_cors import CORS
import grpc
from concurrent import futures
import time
import event_management_pb2
import event_management_pb2_grpc
import mysql.connector
from datetime import datetime

app = Flask(__name__)
CORS(app)

orginazation = {
    "orgId": "1",
    "orgName": "Những thành phố mơ màng",
    "orgLogoURL": "https://salt.tkbcdn.com/ts/ds/be/d4/a4/ec47923339d2a1a6a4d060d1f4caaf18.jpg",
    "orgDescription": "Updating...",
}

class EventManagementServicer(event_management_pb2_grpc.EventManagementServicer):
    def __init__(self):
        try:
            self.db = mysql.connector.connect(
                # host='mysql-db',
                user='root',
                password='123',
                database='event_management',
                port=3306
            )
            self.cursor = self.db.cursor(dictionary=True)
            print("Connected to the database successfully.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.db = None
            self.cursor = None

    def CreateEvent(self, request, context):
        print(request)
        try:
            # Parse and format datetime
            datetime_str = request.datetime + "T00:00:00"  # Assuming you want to set time to 00:00:00
            datetime_obj = datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M:%S')

            # Prepare SQL query
            sql = """
                INSERT INTO Events (name, bannerURL, datetime, minTicketPrice, location, orgId, orgName, orgLogoURL)
                VALUES (%(name)s, %(bannerURL)s, %(datetime)s, %(minTicketPrice)s, %(location)s, %(orgId)s, %(orgName)s, %(orgLogoURL)s)
            """
            params = {
                'name': request.name,
                'bannerURL': request.bannerURL,
                'datetime': datetime_obj,
                'minTicketPrice': request.minTicketPrice,
                'location': request.location,
                'orgId': "1",
                'orgName': "Những thành phố mơ màng",
                'orgLogoURL': "https://salt.tkbcdn.com/ts/ds/be/d4/a4/ec47923339d2a1a6a4d060d1f4caaf18.jpg",
            }

            # Execute SQL query
            self.cursor.execute(sql, params)
            self.db.commit()  # Assuming self.db is your database connection

            # Fetch the last inserted event id
            event_id = self.cursor.lastrowid

            # Return the newly created event as gRPC response
            return event_management_pb2.Event(
                id=event_id,
                name=request.name,
                bannerURL=request.bannerURL,
                datetime=request.datetime,  # Return formatted datetime
                minTicketPrice=request.minTicketPrice,
                location=request.location
            )

        except Exception as e:
            self.db.rollback()  # Rollback the transaction on error
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INTERNAL)
            return event_management_pb2.Event()

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
            sql = "SELECT * FROM Events WHERE 1=1"
            params = {}

            if request.name:
                sql += " AND name LIKE CONCAT('%%', %(name)s, '%%')"
                params['name'] = request.name

            if request.categories:
                sql += " AND categories = %(categories)s"
                params['categories'] = request.categories

            self.cursor.execute(sql, params)
            events = self.cursor.fetchall()
            event_list = []
            for event in events:
                event_list.append(event_management_pb2.Event(
                    id=int(event['id']),
                    name=event['name'],
                    description=event['description'],
                    location=event['location'],
                    datetime=event['datetime'].strftime("%Y-%m-%d %H:%M:%S"),
                    bannerURL=event['bannerURL'],
                    url=event['url'],
                    venue=event['venue'],
                    address=event['address'],
                    minTicketPrice=int(event['minTicketPrice']),
                    categories=event['categories']
                ))
            return event_management_pb2.EventList(events=event_list)
        except Exception as e:
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INTERNAL)
            return event_management_pb2.EventList()

    def GetEventById(self, request, context):
        # Assuming self.cursor is your database cursor
        sql = "SELECT * FROM Events WHERE id = %s"
        self.cursor.execute(sql, (request.id,))
        event = self.cursor.fetchone()

        if not event:
            context.abort(grpc.StatusCode.NOT_FOUND, "Event not found")

        return event(
            id=int(event['id']),
            name=event['name'],
            description=event['description'],
            location=event['location'],
            datetime=event['datetime'].strftime("%Y-%m-%d %H:%M:%S"),
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
        )

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
    server.add_insecure_port('[::]:5002')
    server.start()
    print("gRPC server is running on port 5002...")
    try:
        while True:
            time.sleep(86400)  # Sleep for one day
    except KeyboardInterrupt:
        print("Shutting down gRPC server...")
        server.stop(0)
        print("gRPC server stopped.")

if __name__ == '__main__':
    serve()