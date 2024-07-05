from flask import Blueprint, request, jsonify, make_response
from flask_cors import cross_origin
from proto_generate import ticket_management_pb2, ticket_management_pb2_grpc
import grpc
from models import db, Tickets, Orders, OrderItems, proto_to_ticket, proto_to_order

# Create a Blueprint for routes
bp = Blueprint('routes', __name__)

# Setup gRPC connections
channel = grpc.insecure_channel('localhost:50052')
stub = ticket_management_pb2_grpc.TicketServiceStub(channel)
order_channel = grpc.insecure_channel('localhost:50052')
order_stub = ticket_management_pb2_grpc.OrderServiceStub(order_channel)

@bp.route('/tickets', methods=['POST'])
def add_ticket():
    data = request.json
    ticket_request = ticket_management_pb2.TicketRequest(
        event_id=int(data['event_id']),
        ticket_type=data['ticket_type'],
        ticket_price=float(data['ticket_price']),
        total_quantity=int(data['total_quantity']),
        available_quantity=int(data['available_quantity'])
    )
    try:
        response = stub.AddTicket(ticket_request)
        return jsonify({'ticket': Tickets.to_dict(proto_to_ticket(response.ticket))})
    except grpc.RpcError as e:
        return jsonify({'error': 'Error adding ticket: {}'.format(e.details())}), 500

@bp.route('/tickets/<int:ticket_id>', methods=['PUT'])
def update_ticket(ticket_id):
    data = request.json
    ticket_request = ticket_management_pb2.Ticket(
        ticket_id=ticket_id,
        event_id=int(data['event_id']),
        ticket_type=data['ticket_type'],
        ticket_price=float(data['ticket_price']),
        total_quantity=int(data['total_quantity']),
        available_quantity=int(data['available_quantity'])
    )
    try:
        response = stub.UpdateTicket(ticket_request)
        if response.ticket.ticket_id == 0:
            return jsonify({'error': 'Ticket not found'}), 404
        return jsonify({'ticket': Tickets.to_dict(proto_to_ticket(response.ticket))})
    except grpc.RpcError as e:
        return jsonify({'error': 'Error updating ticket: {}'.format(e.details())}), 500

@bp.route('/tickets', methods=['GET'])
def get_all_tickets():
    try:
        response = stub.GetAllTickets(ticket_management_pb2.GetAllTicketsRequest())
        tickets = [Tickets.to_dict(proto_to_ticket(ticket)) for ticket in response.tickets]
        return jsonify({'tickets': tickets})
    except grpc.RpcError as e:
        return jsonify({'error': 'Error getting tickets: {}'.format(e.details())}), 500

@bp.route('/tickets_by_event/<int:event_id>', methods=['GET'])
def get_all_tickets_by_event(event_id):
    try:
        response = stub.GetAllTicketsByEvent(ticket_management_pb2.GetAllTicketsByEventRequest(event_id=event_id))
        tickets = [Tickets.to_dict(proto_to_ticket(ticket)) for ticket in response.tickets]
        return jsonify({'tickets': tickets})
    except grpc.RpcError as e:
        return jsonify({'error': 'Error getting tickets: {}'.format(e.details())}), 500

@bp.route('/tickets/<int:ticket_id>', methods=['GET'])
def get_ticket_by_id(ticket_id):
    try:
        response = stub.GetTicketById(ticket_management_pb2.GetTicketByIdRequest(ticket_id=ticket_id))
        ticket_dict = Tickets.to_dict(proto_to_ticket(response.ticket))
        return jsonify({'ticket': ticket_dict})
    except grpc.RpcError as e:
        return jsonify({'error': 'Error getting ticket: {}'.format(e.details())}), 500

@bp.route('/tickets/<int:ticket_id>', methods=['DELETE'])
@cross_origin()
def delete_ticket(ticket_id):
    try:
        response = stub.DeleteTicket(ticket_management_pb2.DeleteTicketRequest(ticket_id=ticket_id))
        if response.success:
            return jsonify({'success': True})
        else:
            return jsonify({'error': 'Ticket not found'}), 404
    except grpc.RpcError as e:
        return jsonify({'error': 'Error deleting ticket: {}'.format(e.details())}), 500

@bp.route('/orders', methods=['POST'])
def add_order():
    data = request.json
    items = [ticket_management_pb2.OrderItem(ticket_id=item['ticket_id'], quantity=item['quantity'], price=item['price']) for item in data['items']]
    order_request = ticket_management_pb2.OrderRequest(customer_name=data['customer_name'], items=items, total_price=data['total_price'])
    try:
        response = order_stub.AddOrder(order_request)
        return jsonify({'order': Orders.to_dict(proto_to_order(response.order))})
    except grpc.RpcError as e:
        return jsonify({'error': 'Error adding order: {}'.format(e.details())}), 500

@bp.route('/orders', methods=['GET'])
def get_all_orders():
    try:
        response = order_stub.GetAllOrders(ticket_management_pb2.GetAllOrdersRequest())
        orders = [Orders.to_dict(proto_to_order(order)) for order in response.orders]
        return jsonify({'orders': orders}), 200
    except grpc.RpcError as e:
        return jsonify({'error': 'Error getting orders: {}'.format(e.details())}), 500

@bp.route('/orders/<int:order_id>', methods=['GET'])
def get_order_by_id(order_id):
    try:
        request = ticket_management_pb2.GetOrdersByIdRequest(order_id=order_id)
        response = order_stub.GetOrderById(request)
        order_dict = Orders.to_dict(proto_to_order(response.order))
        return jsonify({'order': order_dict})
    except grpc.RpcError as e:
        return jsonify({'error': 'Error getting order details: {}'.format(e.details())}), 500

@bp.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    try:
        response = order_stub.DeleteOrder(ticket_management_pb2.DeleteOrderRequest(order_id=order_id))
        if response.success:
            return jsonify({'success': True})
        else:
            return jsonify({'error': 'Order not found'}), 404
    except grpc.RpcError as e:
        return jsonify({'error': 'Error deleting order: {}'.format(e.details())}), 500

@bp.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    data = request.json
    order_request = ticket_management_pb2.Order(
        order_id=order_id,
        customer_name=data['customer_name'],
        total_price=data['total_price'],
        status=data['status']
    )
    try:
        response = order_stub.UpdateOrder(order_request)
        if response.order.order_id == 0:
            return jsonify({'error': 'Order not found'}), 404
        return jsonify({'order': Orders.to_dict(proto_to_order(response.order))})
    except grpc.RpcError as e:
        return jsonify({'error': 'Error updating order: {}'.format(e.details())}), 500
