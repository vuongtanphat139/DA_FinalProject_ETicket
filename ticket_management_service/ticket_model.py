from flask_sqlalchemy import SQLAlchemy
import uuid

# Tạo một đối tượng SQLAlchemy để tương tác với cơ sở dữ liệu
db = SQLAlchemy()

# Định nghĩa model Tickets kế thừa từ db.Model
class Tickets(db.Model):
    # Định nghĩa các cột trong bảng 'tickets'
    ticket_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    event_id = db.Column(db.String(36), nullable=False)
    ticket_type = db.Column(db.String(50), nullable=False)
    ticket_price = db.Column(db.Numeric(10, 2), nullable=False)
    total_quantity = db.Column(db.Integer, nullable=False)
    available_quantity = db.Column(db.Integer, nullable=False)

    # Định nghĩa method 'to_dict' để serialize đối tượng thành dictionary
    def to_dict(self):
        return {
            'ticket_id': self.ticket_id,
            'event_id': self.event_id,
            'ticket_type': self.ticket_type,
            'ticket_price': float(self.ticket_price),  # Convert decimal to float for JSON serialization
            'total_quantity': self.total_quantity,
            'available_quantity': self.available_quantity
        }
