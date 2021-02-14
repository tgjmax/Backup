from common.models import SampleRequest, Menus
from main import db


def create_sample_request(customer_name, customer_number, customer_address, pet_name, pet_breed, pet_age,
                          pet_weight):
    db.create_all()
    sample_request = SampleRequest(customer_name=customer_name, customer_number=customer_number
                                   , customer_address=customer_address, pet_name=pet_name, pet_breed=pet_breed,
                                   pet_age=pet_age, pet_weight=pet_weight)
    try:
        db.create_all()
        db.session.add(sample_request)
        db.session.commit()
        return sample_request
    except Exception as e:
        db.session.rollback()
        print(e)
        return None


def create_menus(product_name, net_weight, price, brand, product_for, product_description, product_image, product_type):
    db.create_all()
    menus = Menus(product_name=product_name, net_weight=net_weight, price=price, brand=brand,
                  product_for=product_for, product_description=product_description,
                  product_image=product_image, product_type=product_type)
    try:
        db.create_all()
        db.session.add(menus)
        db.session.commit()
        return menus
    except Exception as e:
        db.session.rollback()
        print(e)
        return None


def get_sample_request(sample_id=None):
    db.create_all()
    if id is None:
        return SampleRequest.query.all()
    else:
        return SampleRequest.query.filter_by(sample_id=sample_id).first()


def get_menus(product_id=None):
    db.create_all()
    if id is None:
        return Menus.query.all()
    else:
        return Menus.query.filter_by(product_id=product_id).first()


def update_sample_request(sample_id, customer_name, customer_number, customer_address, pet_name, pet_breed, pet_age,
                          pet_weight):
    sample_request = get_sample_request(sample_id=sample_id)
    if sample_request is not None:
        if customer_name is not None:
            sample_request.customer_name = customer_name
        if customer_number is not None:
            sample_request.customer_number = customer_number
        if customer_address is not None:
            sample_request.customer_address = customer_address
        if pet_name is not None:
            sample_request.pet_name = pet_name
        if pet_breed is not None:
            sample_request.pet_breed = pet_breed
        if pet_age is not None:
            sample_request.pet_age = pet_age
        if pet_weight is not None:
            sample_request.pet_weight = pet_weight
        try:
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            db.session.rollback()
            return False
    else:
        return False


def update_menus(product_id, product_name, net_weight, price, brand, product_for, product_description, product_image,
                 product_type):
    menus = get_menus(product_id=product_id)
    if menus is not None:
        if product_name is not None:
            menus.product_name = product_name
        if net_weight is not None:
            menus.net_weight = net_weight
        if price is not None:
            menus.price = price
        if brand is not None:
            menus.brand = brand
        if product_for is not None:
            menus.product_for = product_for
        if product_description is not None:
            menus.product_description = product_description
        if product_image is not None:
            menus.product_image = product_image
        if product_type is not None:
            menus.product_type = product_type
        try:
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            db.session.rollback()
            return False
    else:
        return False

def delete_sample_request(sample_id):
    sample_request = get_sample_request(sample_id=sample_id)
    try:
        if sample_request is not None:
            db.session.delete(sample_request)
            db.session.commit()
            return True
        else:
            return False
    except Exception as e:
        db.session.rollback()
        return False
