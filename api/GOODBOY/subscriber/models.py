from main import db
from datetime import datetime


class Subscriber(db.Model):
    sub_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    mobile_number = db.Column(db.String(20), unique=True, nullable=False)
    photo = db.Column(db.String(100))
    lat = db.Column(db.String(50), nullable=False)
    long = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    address = db.Column(db.String(500), nullable=False)
    pet_name = db.Column(db.String(50), nullable=False)
    pet_breed = db.Column(db.String(50), nullable=False)
    package = db.Column(db.String(100), unique=True, nullable=False)
    sub_type = db.Column(db.String(100), nullable=False)
    price = db.Column(db.String(100), nullable=False)
    product = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.DateTime, unique=True, nullable=False, default=datetime.utcnow)

    def to_dict(self):
        return {'sub_id': self.sub_id, 'name': self.name, 'mobile_number': self.mobile_number, 'photo ': self.photo,
                'address': self.address,
                'lat': self.lat, 'long': self.long,
                'email': self.email, 'pet_name': self.pet_name,
                'pet_breed': self.pet_breed, 'package': self.package, 'sub_type': self.sub_type, 'price': self.price,
                'product': self.product, 'start_date': self.start_date}


class Payments(db.Model):
    payment_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    date = db.Column(db.DATE, nullable=False, default=datetime.utcnow())
    # time = db.Column(db.TIME, unique=True, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    product = db.Column(db.String(50), nullable=False)
    sub_type = db.Column(db.String(100), foreign_key=True)
    package = db.Column(db.String(100), foreign_key=True)
    sub_id = db.Column(db.Integer, foreign_key=True)

    def to_dict(self):
        return {'payment_id': self.payment_id, 'date': self.date, 'price': self.price,
                'product': self.product, 'sub_type': self.sub_type, 'package': self.package, 'sub_id': self.sub_id}


class MyOrder(db.Model):
    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    sub_id = db.Column(db.Integer, foreign_key=True)
    product = db.Column(db.String(50), foreign_key=True)
    price = db.Column(db.Integer, foreign_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    payment_id = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {'order_id': self.order_id, 'sub_id': self.sub_id, 'product': self.product, 'price': self.price,
                'quantity': self.quantity, 'payment_id': self.payment_id}


class CancelSub(db.Model):
    sub_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    mobile_number = db.Column(db.String(20), unique=True, nullable=False)
    address = db.Column(db.String(500), nullable=False)
    lat = db.Column(db.String(50), nullable=False)
    long = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    pet_name = db.Column(db.String(50), nullable=False)
    pet_breed = db.Column(db.String(50), nullable=False)
    package = db.Column(db.String(100), unique=True, nullable=False)
    sub_type = db.Column(db.String(100), nullable=False)
    price = db.Column(db.String(100), nullable=False)
    product = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.DateTime, unique=True, nullable=False)
    end_date = db.Column(db.DateTime, unique=True, nullable=False, default=datetime.utcnow)

    def to_dict(self):
        return {'sub_id': self.sub_id, 'name': self.name, 'mobile_number': self.mobile_number, 'address': self.address,
                'lat': self.lat, 'long': self.long,
                'email': self.email, 'pet_name': self.pet_name,
                'pet_breed': self.pet_breed, 'package': self.package, 'sub_type': self.sub_type, 'price': self.price,
                'product': self.product, 'start_date': self.start_date, 'end_date': self.end_date}


class PauseSub(db.Model):
    sub_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    mobile_number = db.Column(db.String(20), unique=True, nullable=False)
    address = db.Column(db.String(500), nullable=False)
    lat = db.Column(db.String(50), nullable=False)
    long = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    pet_name = db.Column(db.String(50), nullable=False)
    pet_breed = db.Column(db.String(50), nullable=False)
    package = db.Column(db.String(100), unique=True, nullable=False)
    sub_type = db.Column(db.String(100), nullable=False)
    price = db.Column(db.String(100), nullable=False)
    product = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.DateTime, unique=True, nullable=False)
    end_date = db.Column(db.DateTime, unique=True, nullable=False, default=datetime.utcnow)

    def to_dict(self):
        return {'sub_id': self.sub_id, 'name': self.name, 'mobile_number': self.mobile_number, 'address': self.address,
                'lat': self.lat, 'long': self.long,
                'email': self.email, 'pet_name': self.pet_name,
                'pet_breed': self.pet_breed, 'package': self.package, 'sub_type': self.sub_type, 'price': self.price,
                'product': self.product, 'start_date': self.start_date, 'end_date': self.end_date}


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    order_id = db.Column(db.Integer, autoincrement=True, nullable=False)
    sub_id = db.Column(db.Integer, foreign_key=True)
    product = db.Column(db.String(50), foreign_key=True)
    price = db.Column(db.Integer, foreign_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    payment_id = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {'order_id': self.order_id, 'sub_id': self.sub_id, 'product': self.product, 'price': self.price,
                'quantity': self.quantity, 'payment_id': self.payment_id}


class Checkout(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    order_id = db.Column(db.Integer, nullable=False)
    sub_id = db.Column(db.Integer, foreign_key=True)
    product = db.Column(db.String(50), foreign_key=True)
    price = db.Column(db.Integer, foreign_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    payment_id = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {'order_id': self.order_id, 'sub_id': self.sub_id, 'product': self.product, 'price': self.price,
                'quantity': self.quantity, 'payment_id': self.payment_id}
