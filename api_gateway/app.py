
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import grpc
from proto_generate import event_management_pb2_grpc
from flask_cors import CORS


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123@localhost/ticket_management'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

def get_grpc_client():
    channel = grpc.insecure_channel('localhost:5002')
    stub = event_management_pb2_grpc.EventManagementStub(channel)
    return stub

# Import routes after initializing app to avoid circular imports
from routes.event_management_routes import *
from routes.ticket_management_routes import *


# Import routes after initializing app to avoid circular imports
if __name__ == '__main__':
    app.run(debug=True, port=5001)
