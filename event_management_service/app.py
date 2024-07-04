from flask import Flask, jsonify, request
from flask_cors import CORS
import grpc
import event_management_pb2
import event_management_pb2_grpc
from datetime import datetime

app = Flask(__name__)
CORS(app)

def get_grpc_client():
    channel = grpc.insecure_channel('localhost:50051')
    stub = event_management_pb2_grpc.EventManagementStub(channel)
    return stub

@app.route('/create_event', methods=['POST'])
def create_event():
    try:
        # Get data from request
        data = request.json

        # Parse and format datetime
        # datetime_str = data['datetime']
        # datetime_obj = datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M:%S')
        # formatted_datetime = datetime_obj.strftime('%Y-%m-%d %H:%M:%S')

        # Initialize gRPC client
        client = get_grpc_client()

        # Prepare gRPC request
        grpc_request = event_management_pb2.CreateEventRequest(
            name=data['name'],
            bannerURL=data['bannerURL'],
            datetime=data['datetime'],  # Use formatted datetime here
            minTicketPrice=data['minTicketPrice'],
            location=data['location']
        )

        # Call gRPC method
        response = client.CreateEvent(grpc_request)

        # Return response as JSON
        return jsonify({
            'id': response.id,
            'name': response.name,
            'bannerURL': response.bannerURL,
            'datetime': response.datetime,  # Assuming response.datetime is correctly formatted
            'minTicketPrice': response.minTicketPrice,
            'location': response.location
        })

    except grpc.RpcError as e:
        return jsonify(error=str(e)), 500

    except Exception as e:
        return jsonify(error=str(e)), 500

@app.route('/update_event', methods=['POST'])
def update_event():
    client = get_grpc_client()
    event_data = request.json
    event = event_management_pb2.Event(
        id=event_data.get('id'),
        name=event_data.get('name'),
        description=event_data.get('description'),
        location=event_data.get('location'),
        datetime=event_data.get('datetime'),
        bannerURL=event_data.get('bannerURL'),
        url=event_data.get('url'),
        venue=event_data.get('venue'),
        address=event_data.get('address'),
        orgId=event_data.get('orgId'),
        minTicketPrice=event_data.get('minTicketPrice'),
        status=event_data.get('status'),
        statusName=event_data.get('statusName'),
        orgLogoURL=event_data.get('orgLogoURL'),
        orgName=event_data.get('orgName'),
        orgDescription=event_data.get('orgDescription'),
        categories=event_data.get('categories')
    )
    try:
        response = client.UpdateEvent(event)
        return jsonify(success=response.success, message=response.message, event={
            'id': response.event.id,
            'name': response.event.name,
            'description': response.event.description,
            'location': response.event.location,
            'datetime': response.event.datetime,
            'bannerURL': response.event.bannerURL,
            'url': response.event.url,
            'venue': response.event.venue,
            'address': response.event.address,
            'orgId': response.event.orgId,
            'minTicketPrice': response.event.minTicketPrice,
            'status': response.event.status,
            'statusName': response.event.statusName,
            'orgLogoURL': response.event.orgLogoURL,
            'orgName': response.event.orgName,
            'orgDescription': response.event.orgDescription,
            'categories': response.event.categories
        })
    except grpc.RpcError as e:
        return jsonify(error=str(e)), 500

@app.route('/get_events', methods=['GET'])
def get_events():
    try:
        client = get_grpc_client()

        # Prepare gRPC request based on query parameters
        grpc_request = event_management_pb2.GetEventRequest(
            name=request.args.get('name', None),
            categories=request.args.get('categories', None)
        )

        # Call gRPC method
        response = client.GetEvent(grpc_request)

        # Prepare JSON response
        events = [{
            'id': e.id,
            'name': e.name,
            'description': e.description,
            'location': e.location,
            'datetime': e.datetime,
            'bannerURL': e.bannerURL,
            'url': e.url,
            'venue': e.venue,
            'address': e.address,
            'minTicketPrice': e.minTicketPrice,
            'categories': e.categories
        } for e in response.events]

        return jsonify(events=events)

    except grpc.RpcError as e:
        return jsonify(error=str(e)), 500

@app.route('/search_events', methods=['POST'])
def search_events():
    client = get_grpc_client()
    criteria = request.json
    search_criteria = event_management_pb2.SearchCriteria(
        date=criteria.get('date'),
        location=criteria.get('location'),
        topic=criteria.get('topic')
    )
    try:
        response = client.SearchEvents(search_criteria)
        events = [{
            'id': e.id,
            'name': e.name,
            'description': e.description,
            'location': e.location,
            'datetime': e.datetime,
            'bannerURL': e.bannerURL,
            'url': e.url,
            'venue': e.venue,
            'address': e.address,
            'orgId': e.orgId,
            'minTicketPrice': e.minTicketPrice,
            'status': e.status,
            'statusName': e.statusName,
            'orgLogoURL': e.orgLogoURL,
            'orgName': e.orgName,
            'orgDescription': e.orgDescription,
            'categories': e.categories
        } for e in response.events]
        return jsonify(events=events)
    except grpc.RpcError as e:
        return jsonify(error=str(e)), 500

    client = get_grpc_client()
    criteria = request.json
    search_criteria = event_management_pb2.SearchCriteria(
        date=criteria.get('date'),
        location=criteria.get('location'),
        topic=criteria.get('topic')
    )
    response = client.SearchEvents(search_criteria)
    events = [{
        'id': e.id,
        'name': e.name,
        'description': e.description,
        'location': e.location,
        'datetime': e.datetime,
        'bannerURL': e.bannerURL,
        'url': e.url,
        'venue': e.venue,
        'address': e.address,
        'orgId': e.orgId,
        'minTicketPrice': e.minTicketPrice,
        'status': e.status,
        'statusName': e.statusName,
        'orgLogoURL': e.orgLogoURL,
        'orgName': e.orgName,
        'orgDescription': e.orgDescription,
        'categories': e.categories
    } for e in response.events]
    return jsonify(events=events)

@app.route('/purchase_ticket', methods=['POST'])
def purchase_ticket():
    client = get_grpc_client()
    ticket_data = request.json
    ticket_request = event_management_pb2.TicketRequest(
        event_id=ticket_data.get('event_id'),
        user_id=ticket_data.get('user_id'),
        quantity=ticket_data.get('quantity')
    )
    try:
        response = client.PurchaseTicket(ticket_request)
        return jsonify(success=response.success, message=response.message)
    except grpc.RpcError as e:
        return jsonify(error=str(e)), 500

@app.route('/get_user_events', methods=['GET'])
def get_user_events():
    client = get_grpc_client()
    user_id = int(request.args.get('id'))
    try:
        response = client.GetUserEvents(event_management_pb2.UserID(id=user_id))
        events = [{
            'id': e.id,
            'name': e.name,
            'description': e.description,
            'location': e.location,
            'datetime': e.datetime,
            'bannerURL': e.bannerURL,
            'url': e.url,
            'venue': e.venue,
            'address': e.address,
            'orgId': e.orgId,
            'minTicketPrice': e.minTicketPrice,
            'status': e.status,
            'statusName': e.statusName,
            'orgLogoURL': e.orgLogoURL,
            'orgName': e.orgName,
            'orgDescription': e.orgDescription,
            'categories': e.categories
        } for e in response.events]
        return jsonify(events=events)
    except grpc.RpcError as e:
        return jsonify(error=str(e)), 500

    client = get_grpc_client()
    user_id = int(request.args.get('id'))
    response = client.GetUserEvents(event_management_pb2.UserID(id=user_id))
    events = [{
        'id': e.id,
        'name': e.name,
        'description': e.description,
        'location': e.location,
        'datetime': e.datetime,
        'bannerURL': e.bannerURL,
        'url': e.url,
        'venue': e.venue,
        'address': e.address,
        'orgId': e.orgId,
        'minTicketPrice': e.minTicketPrice,
        'status': e.status,
        'statusName': e.statusName,
        'orgLogoURL': e.orgLogoURL,
        'orgName': e.orgName,
        'orgDescription': e.orgDescription,
        'categories': e.categories
    } for e in response.events]
    return jsonify(events=events)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
