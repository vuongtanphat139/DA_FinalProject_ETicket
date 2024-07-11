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
                'orgId': 1,
                'orgName': "Những thành phố mơ màng",
                'orgLogoURL': "https://salt.tkbcdn.com/ts/ds/be/d4/a4/ec47923339d2a1a6a4d060d1f4caaf18.jpg",
            }

            # Execute SQL query
            self.cursor.execute(sql, params)
            self.db.commit()  # Assuming self.db is your database connection

            # Fetch the last inserted event id
            event_id = self.cursor.lastrowid
            print(event_id)
            datetime_str = datetime_obj.strftime("%Y-%m-%d %H:%M:%S")

            # Return the newly created event as gRPC response
            return event_management_pb2.Event(
                id=int(event_id),
                name=request.name,
                description="Null",
                location=request.location,
                datetime="2024-07-11 00:00:00",
                bannerURL=request.bannerURL,
                url="Null",
                venue="Null",
                address="Null",
                orgId=1,
                minTicketPrice=int(request.minTicketPrice),
                status="Null",
                statusName="Null",
                orgLogoURL="https://salt.tkbcdn.com/ts/ds/be/d4/a4/ec47923339d2a1a6a4d060d1f4caaf18.jpg",
                orgName="Những thành phố mơ màng",
                orgDescription="Null",
                categories="Null"
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

    def GetEventByOrgId(self, request, context):
        try:
            # Assuming self.cursor is your database cursor
            sql = "SELECT * FROM Events WHERE orgId = %s"
            self.cursor.execute(sql, (request.orgId,))
            events = self.cursor.fetchall()

            if not events:
                context.abort(grpc.StatusCode.NOT_FOUND, "No events found for the given organizationId")

            # Convert events to a list of Event messages
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
        try:
            # Assuming self.cursor is your database cursor
            sql = "SELECT * FROM Events WHERE id = %s"
            self.cursor.execute(sql, (request.id,))
            event = self.cursor.fetchone()
    
            if not event:
                context.abort(grpc.StatusCode.NOT_FOUND, "Event not found")
    
            # Convert datetime to string format
            datetime_str = event['datetime'].strftime("%Y-%m-%d %H:%M:%S")
    
            # Return event details as a gRPC response
            return event_management_pb2.Event(
                id=int(event['id']),
                name=event['name'],
                description=event['description'],
                location=event['location'],
                datetime=datetime_str,
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
    
        except Exception as e:
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INTERNAL)
            return event_management_pb2.Event()
        
    def GetUserEvents(self, request, context):
        try:
            user_id = request.id
            
            # Step 1: Fetch event IDs for the given user ID from UserEvents table
            sql_user_events = "SELECT event_id FROM UserEvents WHERE user_id = %s"
            self.cursor.execute(sql_user_events, (user_id,))
            user_events = self.cursor.fetchall()
            
            if not user_events:
                context.abort(grpc.StatusCode.NOT_FOUND, "No events found for the given userId")
            
            # Step 2: Fetch event details for each event ID from Events table
            event_ids = [ue['event_id'] for ue in user_events]
            sql_events = "SELECT * FROM Events WHERE id IN (%s)" % ','.join(['%s'] * len(event_ids))
            self.cursor.execute(sql_events, event_ids)
            events = self.cursor.fetchall()
            
            if not events:
                context.abort(grpc.StatusCode.NOT_FOUND, "No events found for the given event IDs")
            
            # Step 3: Convert events to a list of Event messages
            event_list = []
            for event in events:
                event_list.append(event_management_pb2.Event(
                    id=int(event['id']) if event['id'] is not None else 0,
                    name=event['name'] or '',
                    description=event['description'] or '',
                    location=event['location'] or '',
                    datetime=event['datetime'].strftime("%Y-%m-%d %H:%M:%S") if event['datetime'] else '',
                    bannerURL=event['bannerURL'] or '',
                    url=event['url'] or '',
                    venue=event['venue'] or '',
                    address=event['address'] or '',
                    orgId=int(event['orgId']) if event['orgId'] is not None else 0,
                    minTicketPrice=int(event['minTicketPrice']) if event['minTicketPrice'] is not None else 0,
                    status=event['status'] or '',
                    statusName=event['statusName'] or '',
                    orgLogoURL=event['orgLogoURL'] or '',
                    orgName=event['orgName'] or '',
                    orgDescription=event['orgDescription'] or '',
                    categories=event['categories'] or ''
                ))
            
            return event_management_pb2.EventList(events=event_list)

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
        
    def CreateUserEvent(self, request, context):
        try:
            user_id = request.user_id
            event_id = request.event_id

            # Prepare SQL query
            sql_insert = "INSERT INTO UserEvents (user_id, event_id) VALUES (%s, %s)"
            self.cursor.execute(sql_insert, (user_id, event_id))
            self.db.commit()

            new_id = self.cursor.lastrowid
            # logging.debug(f"UserEvent created with id: {new_id}")

            return event_management_pb2.UserEventResponse(id=new_id)
        except Exception as e:
            # logging.error(f"Exception occurred: {e}", exc_info=True)
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INTERNAL)
            return event_management_pb2.UserEventResponse()

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