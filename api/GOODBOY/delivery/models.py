from main import db

class Delivery(db.Model):
    did = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    mobile = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    photo = db.Column(db.String(500), unique=True, nullable=False)
    partner_name = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {'did': self.did, 'name': self.name, 'mobile': self.mobile, 'email': self.email, 'photo': self.photo,
                'partner_name': self.partner_name}
