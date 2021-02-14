from main import db


class SampleRequest(db.Model):
    sample_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    customer_name = db.Column(db.String(50), nullable=False)
    customer_number = db.Column(db.String(20), nullable=False)
    customer_address = db.Column(db.String(500), nullable=False)
    pet_name = db.Column(db.String(50), nullable=False)
    pet_breed = db.Column(db.String(100), nullable=False)
    pet_age = db.Column(db.Integer, nullable=False)
    pet_weight = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {'sample_id': self.sample_id, 'customer_name': self.customer_name,
                'customer_number': self.customer_number, 'customer_address': self.customer_address,
                'pet_name': self.pet_name, 'pet_breed': self.pet_breed, 'pet_age': self.pet_age,
                'pet_weight': self.pet_weight}


class Menus(db.Model):
    product_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    product_name = db.Column(db.String(100), nullable=False)
    net_weight = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    brand = db.Column(db.String(50), unique=True, nullable=False)
    product_for = db.Column(db.String(100), unique=True, nullable=False)
    product_description = db.Column(db.String(500), unique=True, nullable=False)
    product_image = db.Column(db.String(500), unique=True, nullable=False)
    product_type = db.Column(db.String(100), unique=True, nullable=False)

    def to_dict(self):
        return {'product_id': self.product_id, 'product_name': self.product_name, 'net_weight': self.net_weight,
                'price': self.price, 'brand': self.brand, 'product_for': self.product_for,
                'product_description': self.product_description, 'product_image': self.product_image,
                'product_type': self.product_type}
