from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json

app = Flask(__name__)
CORS(app)

# Config database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@db/promotion'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Flask migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Promotion(db.Model):
    promotion_id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    event_id = db.Column(db.Integer)
    description = db.Column(db.String(200))
    discount = db.Column(db.Float)
    deleted = db.Column(db.Integer)
    version = db.Column(db.Integer)

    def to_dict(self):
        return {
            'promotion_id': self.promotion_id,
            'event_id' : self.event_id,
            'description': self.description,
            'discount': self.discount,
            'deleted': self.deleted,
            'version': self.version
        }

class Incentive(db.Model):
    incentive_id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    event_id = db.Column(db.Integer)
    discount = db.Column(db.Float)
    description = db.Column(db.String(200))
    deleted = db.Column(db.Integer)
    version = db.Column(db.Integer)

    def __init__(self):
        return {
            'incentive_id': self.incentive_id,
            'event_id' : self.event_id,
            'description': self.description,
            'discount': self.discount,
            'deleted': self.deleted,
            'version': self.version
        }

# Route để lấy tất cả các chương trình khuyến mãi
@app.route('/promotions', methods=['GET'])
def get_promotions():
    promotions = Promotion.query.all()
    return jsonify([promotion.to_dict() for promotion in promotions])

# Route để lấy một chương trình khuyến mãi cụ thể
@app.route('/promotions/<int:promotion_id>', methods=['GET'])
def get_promotion(promotion_id):
    # promotion = Promotion.query.get_or_404(promotion_id)
    # # return jsonify(promotion.to_dict())
    # response = make_response(json.dumps(promotion.to_dict()), 200)
    # response.mimetype = 'application/json'
    # return response
    promotion = Promotion.query.get(promotion_id)
    if promotion is None:
        response = {
            "message": "Promotion not found",
            "status": 404,
            # "data": None
        }
        return make_response(json.dumps(response), 404)
    
    response = {
        "message": "success",
        "status": 200,
        "data": promotion.to_dict()
    }
    return make_response(json.dumps(response), 200)

# Route để tạo một chương trình khuyến mãi mới
@app.route('/promotions', methods=['POST'])
def create_promotion():
    data = request.json
    new_promotion = Promotion(**data)
    db.session.add(new_promotion)
    db.session.commit()
    # return jsonify(new_promotion.to_dict()), 201
    response = make_response(json.dumps(new_promotion.to_dict()), 201)
    response.mimetype = 'application/json'
    return response

# Route để cập nhật thông tin của một chương trình khuyến mãi
@app.route('/promotions/<int:promotion_id>', methods=['PUT'])
def update_promotion(promotion_id):
    promotion = Promotion.query.get_or_404(promotion_id)
    data = request.json

    promotion.event_id = data.get('event_id', promotion.event_id)
    promotion.description = data.get('description', promotion.description)
    promotion.discount = data.get('discount', promotion.discount)
    promotion.deleted = data.get('deleted', promotion.deleted)
    promotion.version = data.get('version', promotion.version)

    db.session.commit()
    return jsonify(promotion.to_dict())

# Route để xóa một chương trình khuyến mãi
@app.route('/promotions/<int:promotion_id>', methods=['DELETE'])
def delete_promotion(promotion_id):
    promotion = Promotion.query.get_or_404(promotion_id)
    db.session.delete(promotion)
    db.session.commit()
    return '', 204

# Route để lấy tất cả các đợt khuyến mãi
@app.route('/incentives', methods=['GET'])
def get_incentives():
    incentives = Incentive.query.all()
    return jsonify([incentive.to_dict() for incentive in incentives])

# Route để lấy một đợt khuyến mãi cụ thể
@app.route('/incentives/<int:incentive_id>', methods=['GET'])
def get_incentive(incentive_id):
    incentive = Incentive.query.get_or_404(incentive_id)
    return jsonify(incentive.to_dict())

# Route để tạo một đợt khuyến mãi mới
@app.route('/incentives', methods=['POST'])
def create_incentive():
    data = request.json
    new_incentive = Incentive(**data)
    db.session.add(new_incentive)
    db.session.commit()
    return jsonify(new_incentive.to_dict()), 201

# Route để cập nhật thông tin của một đợt khuyến mãi
@app.route('/incentives/<int:incentive_id>', methods=['PUT'])
def update_incentive(incentive_id):
    incentive = Incentive.query.get_or_404(incentive_id)
    data = request.json

    incentive.user_id = data.get('user_id', incentive.user_id)
    incentive.discount = data.get('discount', incentive.discount)
    incentive.status = data.get('status', incentive.status)

    db.session.commit()
    return jsonify(incentive.to_dict())

# Route để xóa một đợt khuyến mãi
@app.route('/incentives/<int:incentive_id>', methods=['DELETE'])
def delete_incentive(incentive_id):
    incentive = Incentive.query.get_or_404(incentive_id)
    db.session.delete(incentive)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

