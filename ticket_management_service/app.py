from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS, cross_origin

import grpc
import ticket_management_pb2
import ticket_management_pb2_grpc
# import event_management_pb2_grpc
# import event_management_pb2

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

# Thiết lập kết nối gRPC order service
order_channel = grpc.insecure_channel('localhost:50052')
order_stub = ticket_management_pb2_grpc.OrderServiceStub(order_channel)

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

### 

class Orders(db.Model):
    __tablename__ = 'orders'
    order_id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(255), nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    status = db.Column(db.Enum('pending', 'completed', 'cancelled', name='order_status'), nullable=False, default='pending')

    # Relationship với OrderItems (mối quan hệ một-nhiều)
    items = db.relationship('OrderItems', backref='Orders', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'order_id': self.order_id,
            'customer_name': self.customer_name,
            'total_price': self.total_price,
            'status': self.status,
            'items': [item.to_dict() for item in self.items]
        }

# Định nghĩa model OrderItem (nếu cần thiết)
class OrderItems(db.Model):
    __tablename__ = 'orderitems'
    order_item_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.order_id', ondelete='CASCADE'), nullable=False)
    ticket_id = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            'order_item_id': self.order_item_id,
            'ticket_id': self.ticket_id,
            'quantity': self.quantity,
            'price': self.price
        }



def proto_to_order(proto):
    # Chuyển đổi từ proto Order sang đối tượng Orders và OrderItems
    order = Orders(
        customer_name=proto.customer_name,
        total_price=proto.total_price,
        status=proto.status
    )
    #temp_order = order
    db.session.add(order)
    db.session.flush()
    for item in proto.items:
        orderitems = OrderItems(
            order_id=order.order_id,  # Gán order_id từ đơn hàng cha
            ticket_id=item.ticket_id,
            quantity=item.quantity,
            price=item.price
        )
        db.session.add(orderitems)  # Thêm order_item vào session để lưu vào cơ sở dữ liệu
    
    db.session.flush()  # Lưu tất cả các order_item vào cơ sở dữ liệu

    return order



@app.route('/orders', methods=['POST'])
def add_order():
    data = request.json
    items = [ticket_management_pb2.OrderItem(ticket_id=item['ticket_id'], quantity=item['quantity'], price=item['price']) for item in data['items']]
    order_request = ticket_management_pb2.OrderRequest(customer_name=data['customer_name'], items=items, total_price=data['total_price'])
    
    try:
        response = order_stub.AddOrder(order_request)
        return jsonify({'order': Orders.to_dict(proto_to_order(response.order))})
    except grpc.RpcError as e:
        return jsonify({'error': 'Error adding order: {}'.format(e.details())}), 500

@app.route('/orders', methods=['GET'])
def get_all_orders():
    try:
        response = order_stub.GetAllOrders(ticket_management_pb2.GetAllOrdersRequest())
        orders = [Orders.to_dict(proto_to_order(order)) for order in response.orders]
        return jsonify({'orders': orders})
    except grpc.RpcError as e:
        return jsonify({'error': 'Error getting orders: {}'.format(e.details())}), 500

@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    try:
        response = order_stub.DeleteOrder(ticket_management_pb2.DeleteOrderRequest(order_id=order_id))
        if response.success:
            return jsonify({'success': True})
        else:
            return jsonify({'error': 'Order not found'}), 404
    except grpc.RpcError as e:
        return jsonify({'error': 'Error deleting order: {}'.format(e.details())}), 500
if __name__ == '__main__':
    app.run(debug=True, port=5001)
