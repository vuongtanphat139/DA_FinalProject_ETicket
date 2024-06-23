from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
import grpc
import ticket_management_pb2
import ticket_management_pb2_grpc
import event_management_pb2_grpc
import event_management_pb2

# Khởi tạo đối tượng Flask để tạo ứng dụng
app = Flask(__name__)
CORS(app)

# Cấu hình kết nối với cơ sở dữ liệu
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/tickets'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Khởi tạo SQLAlchemy và Flask-Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Định nghĩa model Tickets
class Tickets(db.Model):
    ticket_id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.String(50))
    ticket_type = db.Column(db.String(50))
    ticket_price = db.Column(db.Float)
    total_quantity = db.Column(db.Integer)
    available_quantity = db.Column(db.Integer)

    def to_dict(self):
        return {
            'ticket_id': self.ticket_id,
            'event_id': self.event_id,
            'ticket_type': self.ticket_type,
            'ticket_price': self.ticket_price,
            'total_quantity': self.total_quantity,
            'available_quantity': self.available_quantity
        }

# Chuyển đổi giữa model và protobuf
def ticket_to_proto(ticket):
    return ticket_management_pb2.Ticket(
        ticket_id=ticket.ticket_id,
        event_id=ticket.event_id,
        ticket_type=ticket.ticket_type,
        ticket_price=ticket.ticket_price,
        total_quantity=ticket.total_quantity,
        available_quantity=ticket.available_quantity
    )

def proto_to_ticket(proto):
    return Tickets(
        ticket_id=proto.ticket_id,
        event_id=proto.event_id,
        ticket_type=proto.ticket_type,
        ticket_price=proto.ticket_price,
        total_quantity=proto.total_quantity,
        available_quantity=proto.available_quantity
    )

# Thiết lập kết nối gRPC ticket service
channel = grpc.insecure_channel('localhost:50052')
stub = ticket_management_pb2_grpc.TicketServiceStub(channel)

#  # Thiết lập kết nối gRPC event service
# channel = grpc.insecure_channel('localhost:50051')
# stub = event_management_pb2_grpc.EventManagementStub(channel)


# Định nghĩa các route cho Flask
@app.route('/tickets', methods=['POST'])
def add_ticket():
    data = request.json
    ticket_request = ticket_management_pb2.TicketRequest(
        event_id=data['event_id'],
        ticket_type=data['ticket_type'],
        ticket_price=data['ticket_price'],
        total_quantity=data['total_quantity'],
        available_quantity=data['available_quantity']
    )
    try:
        response = stub.AddTicket(ticket_request)
        # Chuyển đổi response.ticket sang dict trước khi trả về
        return jsonify({'ticket': Tickets.to_dict(proto_to_ticket(response.ticket))})
    except grpc.RpcError as e:
        return jsonify({'error': 'Error adding ticket: {}'.format(e.details())}), 500

@app.route('/tickets/<int:ticket_id>', methods=['PUT'])
def update_ticket(ticket_id):
    data = request.json
    ticket_request = ticket_management_pb2.Ticket(
        ticket_id=ticket_id,
        event_id=data['event_id'],
        ticket_type=data['ticket_type'],
        ticket_price=data['ticket_price'],
        total_quantity=data['total_quantity'],
        available_quantity=data['available_quantity']
    )
    try:
        response = stub.UpdateTicket(ticket_request)
        if response.ticket.ticket_id == 0:
            return jsonify({'error': 'Ticket not found'}), 404
        return jsonify({'ticket': Tickets.to_dict(proto_to_ticket(response.ticket))})
    except grpc.RpcError as e:
        return jsonify({'error': 'Error updating ticket: {}'.format(e.details())}), 500

@app.route('/tickets', methods=['GET'])
def get_all_tickets():
    try:
        response = stub.GetAllTickets(ticket_management_pb2.GetAllTicketsRequest())
        tickets = [Tickets.to_dict(proto_to_ticket(ticket)) for ticket in response.tickets]
        return jsonify({'tickets': tickets})
    except grpc.RpcError as e:
        return jsonify({'error': 'Error getting tickets: {}'.format(e.details())}), 500

@app.route('/tickets/<int:ticket_id>', methods=['DELETE'])
def delete_ticket(ticket_id):
    try:
        response = stub.DeleteTicket(ticket_management_pb2.DeleteTicketRequest(ticket_id=ticket_id))
        if response.success:
            return jsonify({'success': True})
        else:
            return jsonify({'error': 'Ticket not found'}), 404
    except grpc.RpcError as e:
        return jsonify({'error': 'Error deleting ticket: {}'.format(e.details())}), 500


# @app.route('/get_events', methods=['GET'])
# def get_events():
#     client = get_grpc_client()
#     try:
#         response = client.GetEvent(event_management_pb2.Empty())
#         events = [{
#             'id': e.id,
#             'name': e.name,
#             'description': e.description,
#             'location': e.location,
#             'datetime': e.datetime,
#             'bannerURL': e.bannerURL,
#             'url': e.url,
#             'venue': e.venue,
#             'address': e.address,
#             'orgId': e.orgId,
#             'minTicketPrice': e.minTicketPrice,
#             'status': e.status,
#             'statusName': e.statusName,
#             'orgLogoURL': e.orgLogoURL,
#             'orgName': e.orgName,
#             'orgDescription': e.orgDescription,
#             'categories': e.categories
#         } for e in response.events]
#         return jsonify(events=events)
#     except grpc.RpcError as e:
#         return jsonify(error=str(e)), 500

# # Định nghĩa route cho get events
# @app.route('/get_events', methods=['GET'])
# def get_events():
#     client = get_grpc_client()
#     try:
#         response = client.GetEvent(event_management_pb2.Empty())
#         events = [{
#             'id': e.id,
#             'name': e.name,
#             'description': e.description,
#             'location': e.location,
#             'datetime': e.datetime,
#             'bannerURL': e.bannerURL,
#             'url': e.url,
#             'venue': e.venue,
#             'address': e.address,
#             'orgId': e.orgId,
#             'minTicketPrice': e.minTicketPrice,
#             'status': e.status,
#             'statusName': e.statusName,
#             'orgLogoURL': e.orgLogoURL,
#             'orgName': e.orgName,
#             'orgDescription': e.orgDescription,
#             'categories': e.categories
#         } for e in response.events]
#         return jsonify(events=events)
#     except grpc.RpcError as e:
#         return jsonify(error=str(e)), 500


if __name__ == '__main__':
    app.run(debug=True, port=5001)
