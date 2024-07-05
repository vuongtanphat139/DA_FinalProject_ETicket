from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Tickets(db.Model):
    ticket_id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer)
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

class Orders(db.Model):
    __tablename__ = 'orders'
    order_id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(255), nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    status = db.Column(db.Enum('pending', 'completed', 'cancelled', name='order_status'), nullable=False, default='pending')

    items = db.relationship('OrderItems', backref='Orders', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'order_id': self.order_id,
            'customer_name': self.customer_name,
            'total_price': self.total_price,
            'status': self.status,
            'items': [item.to_dict() for item in self.items]
        }

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

def proto_to_ticket(proto):
    return Tickets(
        ticket_id=proto.ticket_id,
        event_id=proto.event_id,
        ticket_type=proto.ticket_type,
        ticket_price=proto.ticket_price,
        total_quantity=proto.total_quantity,
        available_quantity=proto.available_quantity
    )

def proto_to_order(proto):
    order = Orders(
        order_id=proto.order_id,
        customer_name=proto.customer_name,
        total_price=proto.total_price,
        status=proto.status
    )
    for item_proto in proto.items:
        order_item = OrderItems(
            order_item_id=item_proto.order_item_id,
            ticket_id=item_proto.ticket_id,
            quantity=item_proto.quantity,
            price=item_proto.price
        )
        order.items.append(order_item)
    return order
