
from flask import Flask
import grpc
from proto_generate import event_management_pb2_grpc
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

def get_grpc_client():
    channel = grpc.insecure_channel('localhost:5002')
    stub = event_management_pb2_grpc.EventManagementStub(channel)
    return stub

# Import routes after initializing app to avoid circular imports
from routes.event_management_routes import *

# Import routes after initializing app to avoid circular imports
if __name__ == '__main__':
    app.run(debug=True, port=5001)
