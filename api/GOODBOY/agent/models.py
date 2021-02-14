from main import db


class Agent(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    mobile_number = db.Column(db.String(20), unique=True, nullable=False)
    address = db.Column(db.String(500), nullable=False)
    business_name = db.Column(db.String(100), nullable=False)
    photo = db.Column(db.String(500), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    type = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'mobile_number': self.mobile_number, 'address': self.address,
                'business_name': self.business_name, 'photo': self.photo, 'email': self.email, 'type': self.type}


class Request(db.Model):
    __tablename__ = 'agent_request'
    request_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    agent_id = db.Column(db.Integer,nullable=False)
    product_id = db.Column(db.Integer, unique=True, nullable=False)
    customer_name = db.Column(db.String(50), nullable=False)
    customer_number = db.Column(db.String(20), unique=True, nullable=False)
    customer_address = db.Column(db.String(500), nullable=False)
    customer_email = db.Column(db.String(100), unique=True, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {'request_id': self.request_id,'agent_id':self.agent_id, 'product_id': self.product_id, 'customer_name': self.customer_name,
                'customer_number': self.customer_number, 'customer_address': self.customer_address,
                'customer_email': self.customer_email, 'quantity': self.quantity}


class Earnings(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    date = db.Column(db.DATETIME, nullable=False)
    #time = db.Column(db.TIME, nullable=False)
    product_id = db.Column(db.Integer, foreign_key=True)
    request_id = db.Column(db.Integer, foreign_key=True)
    price = db.Column(db.Integer, nullable=False)
    earnings = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {'id': self.id, 'date': self.date, 'product_id': self.product_id,
                'request_id': self.request_id, 'price': self.price, 'earnings': self.earnings}
