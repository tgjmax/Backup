from subscriber.models import Subscriber, Payments, MyOrder, CancelSub, PauseSub, Cart, Checkout
from main import db
from utils import upload_file


def create_subscriber(name, mobile_number, address, email, photo, lat, long, pet_name, pet_breed, package, sub_type,
                      price,
                      product):
    db.create_all()
    subscriber = Subscriber(name=name, mobile_number=mobile_number, address=address, email=email, photo=photo, lat=lat,
                            long=long,
                            pet_name=pet_name, pet_breed=pet_breed, package=package, sub_type=sub_type, price=price,
                            product=product)
    try:
        db.create_all()
        db.session.add(subscriber)
        db.session.commit()

        from pathlib import Path
        subscriber.photo = upload_file(
            '{}/PycharmProjects/GOODBOY/uploads/subscribers/{}/'.format(str(Path.home()), subscriber.sub_id),
            file=photo, type='subscribers', id=subscriber.sub_id)
        db.session.add(subscriber)
        db.session.commit()
        return subscriber
    except Exception as e:
        db.session.rollback()
        print(e)
        return None


def create_payments(price, product, sub_type, package, sub_id):
    db.create_all()
    payments = Payments(price=price, product=product, sub_type=sub_type, package=package,
                        sub_id=sub_id)
    try:
        db.create_all()
        db.session.add(payments)
        db.session.commit()
        return payments
    except Exception as e:
        db.session.rollback()
        print(e)
        return None


def create_my_order(sub_id, product, price, quantity, payment_id):      #creating my orders
    db.create_all()
    my_order = MyOrder(sub_id=sub_id, product=product, price=price, quantity=quantity, payment_id=payment_id)
    try:
        db.create_all()
        db.session.add(my_order)
        db.session.commit()
        return my_order
    except Exception as e:
        db.session.rollback()
        print(e)
        return None


def create_cancel_sub(name, mobile_number, address, email, photo, lat, long, pet_name, pet_breed, package, sub_type,
                      price,
                      product, start_date):
    db.create_all()
    cancel_sub = CancelSub(name=name, mobile_number=mobile_number, address=address, email=email, photo=photo, lat=lat,
                           long=long,
                           pet_name=pet_name, pet_breed=pet_breed, package=package, sub_type=sub_type, price=price,
                           product=product, start_date=start_date)

    try:
        db.create_all()
        db.session.add(cancel_sub)
        db.session.commit()
        return cancel_sub
    except Exception as e:
        db.session.rollback()
        print(e)
        return None


def create_pause_sub(name, mobile_number, address, email, photo, lat, long, pet_name, pet_breed, package, sub_type,
                     price,
                     product, start_date):
    db.create_all()
    pause_sub = PauseSub(name=name, mobile_number=mobile_number, address=address, email=email, photo=photo, lat=lat,
                         long=long,
                         pet_name=pet_name, pet_breed=pet_breed, package=package, sub_type=sub_type, price=price,
                         product=product, start_date=start_date)

    try:
        db.create_all()
        db.session.add(pause_sub)
        db.session.commit()
        return pause_sub
    except Exception as e:
        db.session.rollback()
        print(e)
        return None


def create_cart(sub_id, product, price, quantity, payment_id):
    db.create_all()
    cart = Cart(sub_id=sub_id, product=product, price=price, quantity=quantity,
                payment_id=payment_id)
    try:
        db.create_all()
        db.session.add(cart)
        db.session.commit()
        return cart
    except Exception as e:
        db.session.rollback()
        print(e)
        return None


def create_checkout(sub_id, product, price, quantity, payment_id):
    db.create_all()
    checkout = Checkout(sub_id=sub_id, product=product, price=price, quantity=quantity,
                        payment_id=payment_id)
    try:
        db.create_all()
        db.session.add(checkout)
        db.session.commit()
        return checkout
    except Exception as e:
        db.session.rollback()
        print(e)
        return None


def get_subscriber(sub_id=None, mobile=None):
    db.create_all()
    if mobile is None and sub_id is None:
        return Subscriber.query.all()
    elif mobile is None:
        return Subscriber.query.filter_by(sub_id=sub_id).first()
    else:
        return Subscriber.query.filter_by(mobile_number=mobile).first()


def get_payments(payment_id=None):
    db.create_all()
    if payment_id is None:
        return Payments.query.all()
    else:
        return Payments.query.filter_by(payment_id=payment_id).first()


def get_my_order(order_id=None):
    db.create_all()
    if order_id is None:
        return MyOrder.query.all()
    else:
        return MyOrder.query.filter_by(order_id=order_id).first()


def get_pause_sub(sub_id=None):
    db.create_all()
    if sub_id is None:
        return PauseSub.query.all()
    else:
        return PauseSub.query.filter_by(sub_id=sub_id).first()


def get_cancel_sub(sub_id=None):
    db.create_all()
    if sub_id is None:
        return CancelSub.query.all()
    else:
        return CancelSub.query.filter_by(sub_id=sub_id).first()


def get_cart(sub_id=None):
    db.create_all()
    if sub_id is None:
        return Cart.query.all()
    else:
        return Cart.query.filter_by(sub_id=sub_id).first()


def get_checkout(sub_id=None):
    db.create_all()
    if sub_id is None:
        return Checkout.query.all()
    else:
        return Checkout.query.filter_by(sub_id=sub_id).first()


def update_subscriber(sub_id, name, mobile_number, address, email, photo, lat, long, pet_name, pet_breed, package,
                      sub_type,
                      price, product, start_date):
    subscriber = get_subscriber(sub_id=sub_id)
    if subscriber is not None:
        if name is not None:
            subscriber.name = name
        if mobile_number is not None:
            subscriber.mobile_number = mobile_number
        if address is not None:
            subscriber.address = address
        if photo is not None:
            subscriber.photo = photo
        if lat is not None:
            subscriber.lat = lat
        if long is not None:
            subscriber.long = long
        if email is not None:
            subscriber.email = email
        if pet_name is not None:
            subscriber.pet_name = pet_name
        if pet_breed is not None:
            subscriber.pet_breed = pet_breed
        if package is not None:
            subscriber.package = package
        if sub_type is not None:
            subscriber.sub_type = sub_type
        if price is not None:
            subscriber.price = price
        if product is not None:
            subscriber.product = product
        if start_date is not None:
            subscriber.start_date = start_date
        try:
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            db.session.rollback()
            return False
    else:
        return False


def update_payments(payment_id, price, product, sub_type, package, sub_id):
    payments = get_payments(payment_id=payment_id)
    if payments is not None:
        if price is not None:
            payments.price = price
        if product is not None:
            payments.product = product
        if sub_type is not None:
            payments.sub_type = sub_type
        if package is not None:
            payments.package = package
        if sub_type is not None:
            payments.sub_type = sub_type
        try:
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            db.session.rollback()
            return False
    else:
        return False


def update_my_order(order_id, sub_id, product, price, quantity, payment_id):
    my_order = get_my_order(order_id=order_id)
    if my_order is not None:
        if sub_id is not None:
            my_order.sub_id = sub_id
        if product is not None:
            my_order.product = product
        if price is not None:
            my_order.price = price
        if quantity is not None:
            my_order.quantity = quantity
        if payment_id is not None:
            my_order.payment_id = payment_id
        try:
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            db.session.rollback()
            return False
    else:
        return False


def update_cancel_sub(sub_id, name, mobile_number, address, email, photo, lat, long, pet_name, pet_breed, package,
                      sub_type,
                      price, product, start_date):
    cancel_sub = get_cancel_sub(sub_id=sub_id)
    if cancel_sub is not None:
        if name is not None:
            cancel_sub.name = name
        if mobile_number is not None:
            cancel_sub.mobile_number = mobile_number
        if address is not None:
            cancel_sub.address = address
        if photo is not None:
            cancel_sub.photo = photo
        if lat is not None:
            cancel_sub.lat = lat
        if long is not None:
            cancel_sub.long = long
        if email is not None:
            cancel_sub.email = email
        if pet_name is not None:
            cancel_sub.pet_name = pet_name
        if pet_breed is not None:
            cancel_sub.pet_breed = pet_breed
        if package is not None:
            cancel_sub.package = package
        if sub_type is not None:
            cancel_sub.sub_type = sub_type
        if price is not None:
            cancel_sub.price = price
        if product is not None:
            cancel_sub.product = product
        if start_date is not None:
            cancel_sub.start_date = start_date
        try:
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            db.session.rollback()
            return False
    else:
        return False


def update_pause_sub(sub_id, name, mobile_number, address, photo, email, lat, long, pet_name, pet_breed, package,
                     sub_type,
                     price, product, start_date, end_date):
    pause_sub = get_pause_sub(sub_id=sub_id)
    if pause_sub is not None:
        if name is not None:
            pause_sub.name = name
        if mobile_number is not None:
            pause_sub.mobile_number = mobile_number
        if address is not None:
            pause_sub.address = address
        if photo is not None:
            pause_sub.photo = photo
        if lat is not None:
            pause_sub.lat = lat
        if long is not None:
            pause_sub.long = long
        if email is not None:
            pause_sub.email = email
        if pet_name is not None:
            pause_sub.pet_name = pet_name
        if pet_breed is not None:
            pause_sub.pet_breed = pet_breed
        if package is not None:
            pause_sub.package = package
        if sub_type is not None:
            pause_sub.sub_type = sub_type
        if price is not None:
            pause_sub.price = price
        if product is not None:
            pause_sub.product = product
        if start_date is not None:
            pause_sub.start_date = start_date
        if end_date is not None:
            pause_sub.end_date = end_date
        try:
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            db.session.rollback()
            return False
    else:
        return False


def update_cart(order_id, sub_id, product, price, quantity, payment_id):
    cart = get_cart(sub_id=sub_id)
    if cart is not None:
        if sub_id is not None:
            cart.sub_id = sub_id
        if product is not None:
            cart.product = product
        if price is not None:
            cart.price = price
        if quantity is not None:
            cart.quantity = quantity
        if payment_id is not None:
            cart.payment_id = payment_id
        try:
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            db.session.rollback()
            return False
    else:
        return False


def update_checkout(sub_id, product, price, quantity, payment_id): #update for checkout
    checkout = get_checkout(sub_id=sub_id)
    if checkout is not None:
        if sub_id is not None:
            checkout.sub_id = sub_id
        if product is not None:
            checkout.product = product
        if price is not None:
            checkout.price = price
        if quantity is not None:
            checkout.quantity = quantity
        if payment_id is not None:
            checkout.payment_id = payment_id
        try:
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            db.session.rollback()
            return False
    else:
        return False


def delete_subscriber(sub_id):      #deleting subscriber details
    subscriber = get_subscriber(sub_id=sub_id)
    try:
        if subscriber is not None:
            db.session.delete(subscriber)
            db.session.commit()
            return True
        else:
            return False
    except Exception as e:
        db.session.rollback()
        return False


def delete_pause_sub(sub_id):       #deleting paused subscriber data
    pause_sub = get_pause_sub(sub_id=sub_id)
    try:
        if pause_sub is not None:
            db.session.delete(pause_sub)
            db.session.commit()
            return True
        else:
            return False
    except Exception as e:
        db.session.rollback()
        return False


def delete_cancel_sub(sub_id):
    cancel_sub = get_cancel_sub(sub_id=sub_id)
    try:
        if cancel_sub is not None:
            db.session.delete(cancel_sub)
            db.session.commit()
            return True
        else:
            return False
    except Exception as e:
        db.session.rollback()
        return False


def delete_cart(sub_id):
    cart = get_cart(sub_id=sub_id)
    try:
        if cart is not None:
            db.session.delete(cart)
            db.session.commit()
            return True
        else:
            return False
    except Exception as e:
        db.session.rollback()
        return False


def delete_checkout(sub_id):        #delete checkout
    checkout = get_checkout(sub_id=sub_id)
    try:
        if checkout is not None:
            db.session.delete(checkout)
            db.session.commit()
            return True
        else:
            return False
    except Exception as e:
        db.session.rollback()
        return False
