from flask import Flask, request, jsonify
import grpc
import event_management_pb2
import event_management_pb2_grpc

app = Flask(__name__)

def get_grpc_client():
    channel = grpc.insecure_channel('localhost:50051')
    stub = event_management_pb2_grpc.EventManagementStub(channel)
    return stub

@app.route('/create_event', methods=['POST'])
def create_event():
    client = get_grpc_client()
    event_data = request.json
    event = event_management_pb2.Event(
        id=event_data.get('id'),
        name=event_data.get('name'),
        description=event_data.get('description'),
        location=event_data.get('location'),
        datetime=event_data.get('datetime')
    )
    response = client.CreateEvent(event)
    return jsonify(success=response.success, message=response.message, event=response.event)

@app.route('/update_event', methods=['POST'])
def update_event():
    client = get_grpc_client()
    event_data = request.json
    event = event_management_pb2.Event(
        id=event_data.get('id'),
        name=event_data.get('name'),
        description=event_data.get('description'),
        location=event_data.get('location'),
        datetime=event_data.get('datetime')
    )
    response = client.UpdateEvent(event)
    return jsonify(success=response.success, message=response.message, event=response.event)

@app.route('/get_event', methods=['GET'])
def get_event():
    client = get_grpc_client()
    event_id = int(request.args.get('id'))
    response = client.GetEvent(event_management_pb2.EventID(id=event_id))
    return jsonify(id=response.id, name=response.name, description=response.description, location=response.location, datetime=response.datetime)

@app.route('/search_events', methods=['POST'])
def search_events():
    client = get_grpc_client()
    criteria = request.json
    search_criteria = event_management_pb2.SearchCriteria(
        date=criteria.get('date'),
        location=criteria.get('location'),
        topic=criteria.get('topic')
    )
    response = client.SearchEvents(search_criteria)
    events = [{'id': e.id, 'name': e.name, 'description': e.description, 'location': e.location, 'datetime': e.datetime} for e in response.events]
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
    response = client.PurchaseTicket(ticket_request)
    return jsonify(success=response.success, message=response.message)

@app.route('/get_user_events', methods=['GET'])
def get_user_events():
    client = get_grpc_client()
    user_id = int(request.args.get('id'))
    response = client.GetUserEvents(event_management_pb2.UserID(id=user_id))
    events = [{'id': e.id, 'name': e.name, 'description': e.description, 'location': e.location, 'datetime': e.datetime} for e in response.events]
    return jsonify(events=events)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
