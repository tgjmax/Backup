import datetime

from flask import Blueprint, request, jsonify

subscriber_bp = Blueprint('flask_app_bp', __name__,
                          template_folder='templates')

from subscriber.helpers import get_subscriber, create_subscriber, update_subscriber, get_payments, create_payments, \
    update_payments, get_my_order, create_my_order, update_my_order, get_cancel_sub, create_cancel_sub, \
    update_cancel_sub, create_pause_sub, update_pause_sub, get_cart, get_checkout, create_cart, create_checkout, \
    update_cart, update_checkout, get_pause_sub, delete_subscriber, delete_cancel_sub, delete_pause_sub


@subscriber_bp.route("/subscribers", methods=['GET'])
def get_all_subscribers():  # get method for all agents
    if request.method == 'GET':
        subscribers = get_subscriber()
        if subscribers is not None:
            return jsonify([subscriber.to_dict() for subscriber in subscribers])
        return '', 404


@subscriber_bp.route("/subscriber/<id>", methods=['GET', 'POST', 'PUT', 'DELETE'])
def get_or_modify_subscriber(id):  # get method for subscriber
    if request.method == 'GET':
        sub_id = request.args.get('sub_id')
        mobile = request.args.get('mobile')
        subscriber = get_subscriber(sub_id=id, mobile=mobile)
        if subscriber is not None:
            return jsonify(subscriber.to_dict())
        return '', 404

    elif request.method == 'POST':  # agent post method(create)
        name = request.form.get('name')
        mobile_number = request.form.get('mobile')
        address = request.form.get('address')
        lat = request.form.get('lat')
        image = request.files['image']
        long = request.form.get('long')
        email = request.form.get('email')
        pet_name = request.form.get('pet_name')
        pet_breed = request.form.get('pet_breed')
        package = request.form.get('package')
        sub_type = request.form.get('sub_type')
        price = request.form.get('price')
        product = request.form.get('product')
        # start_date = request.form.get('start_date')
        subscriber = create_subscriber(name=name, mobile_number=mobile_number, address=address, photo=image, lat=lat,
                                       long=long,
                                       email=email, pet_name=pet_name, pet_breed=pet_breed, package=package,
                                       sub_type=sub_type, price=price, product=product)
        if subscriber is not None:
            return jsonify(subscriber.to_dict())
        else:
            return 'Duplicate entry', 403

    elif request.method == 'PUT':  # put for agent(update)
        sub_id = request.form.get('sub_id')
        name = request.form.get('name')
        mobile_number = request.form.get('mobile')
        address = request.form.get('address')
        photo = request.form.get('photo')
        email = request.form.get('email')
        lat = request.form.get('lat')
        long = request.form.get('long')
        pet_name = request.form.get('pet_name')
        pet_breed = request.form.get('pet_breed')
        package = request.form.get('package')
        sub_type = request.form.get('sub_type')
        price = request.form.get('price')
        product = request.form.get('product')
        start_date = request.form.get('start_date')
        is_updated = update_subscriber(sub_id=sub_id, name=name, mobile_number=mobile_number, address=address,
                                       email=email, photo=photo,
                                       lat=lat, long=long, pet_name=pet_name, pet_breed=pet_breed, package=package,
                                       sub_type=sub_type, price=price, product=product, start_date=start_date)
        if is_updated:
            return '', 204
        else:
            return '', 400

    elif request.method == 'DELETE':
        sub_id = request.form.get('sub_id')
        is_deleted = delete_subscriber(sub_id=sub_id)
        if is_deleted:
            return '', 204
        else:
            return '', 400


@subscriber_bp.route("/subscriber/payments", methods=['GET'])
def get_all_payments():  # get method for agent request
    if request.method == 'GET':
        payments = get_payments(payment_id=None)
        if payments is not None:
            if isinstance(payments, list):
                return jsonify([payment.to_dict() for payment in payments])
            return jsonify(payments.to_dict())
        return '', 404


@subscriber_bp.route("/subscriber/payment", methods=['GET', 'POST', 'PUT'])
def get_or_modify_payments():  # get method for agent request
    if request.method == 'GET':
        payment_id = request.args.get('payment_id')
        payments = get_payments(payment_id=payment_id)
        if payments is not None:
            return jsonify(payments.to_dict())
        return '', 404

    elif request.method == 'POST':  # post method for payments
        # date = datetime.utcnow()
        # time = request.form.get('time')
        price = request.form.get('price')
        product = request.form.get('product')
        sub_type = request.form.get('sub_type')
        package = request.form.get('package')
        sub_id = request.form.get('sub_id')
        payments = create_payments(price=price, product=product, sub_type=sub_type,
                                   package=package, sub_id=sub_id)
        if payments is not None:
            return jsonify(payments.to_dict())
        else:
            return '', 403

    elif request.method == 'PUT':  # put method for agent_request
        payment_id = request.form.get('payment_id')
        # date = datetime.utcnow()
        # time = request.form.get('time')
        price = request.form.get('price')
        product = request.form.get('product')
        sub_type = request.form.get('sub_type')
        package = request.form.get('package')
        sub_id = request.form.get('sub_id')
        is_updated = update_payments(payment_id=payment_id, price=price, product=product,
                                     sub_type=sub_type, package=package, sub_id=sub_id)
        if is_updated:
            return '', 204
        else:
            return '', 400


@subscriber_bp.route("/subscriber/myorders", methods=['GET'])
def get_all_myorder():  # get method for agent request
    if request.method == 'GET':
        my_orders = get_my_order(order_id=None)
        if my_orders is not None:
            if isinstance(my_orders, list):
                return jsonify([order.to_dict() for order in my_orders])
        return '', 404


@subscriber_bp.route("/subscriber/myorder", methods=['GET', 'POST', 'PUT'])
def get_or_modify_my_order():  # get method for earnings
    if request.method == 'GET':
        order_id = request.args.get('order_id')
        myorder = get_my_order(order_id=order_id)
        if myorder is not None:
            return jsonify(myorder.to_dict())
        return '', 404

    elif request.method == 'POST':  # post method for my order
        sub_id = request.form.get('sub_id')
        product = request.form.get('product')
        price = request.form.get('price')
        quantity = request.form.get('quantity')
        payment_id = request.form.get('payment_id')
        myorder = create_my_order(sub_id=sub_id, product=product, price=price,
                                  quantity=quantity, payment_id=payment_id)
        if myorder is not None:
            return jsonify(myorder.to_dict())
        else:
            return '', 403

    elif request.method == 'PUT':  # put method for  my orders
        order_id = request.form.get('order_id')
        sub_id = request.form.get('sub_id')
        product = request.form.get('product')
        price = request.form.get('price')
        quantity = request.form.get('quantity')
        payment_id = request.form.get('payment_id')
        is_updated = update_my_order(order_id=order_id, sub_id=sub_id, product=product, price=price, quantity=quantity,
                                     payment_id=payment_id)
        if is_updated:
            return '', 204
        else:
            return '', 400


@subscriber_bp.route("/subscriber/cancels", methods=['GET'])
def get_all_cancel_sub():  # get method for agent request
    if request.method == 'GET':
        cancel_subs = get_cancel_sub(sub_id=None)
        if cancel_subs is not None:
            if isinstance(cancel_subs, list):
                return jsonify([cancel_sub.to_dict() for cancel_sub in cancel_subs])
            return jsonify(cancel_subs.to_dict())
        return '', 404


@subscriber_bp.route("/subscriber/cancel", methods=['GET', 'POST', 'PUT', 'DELETE'])
def get_or_modify_cancel_sub():  # get method for agent
    if request.method == 'GET':
        sub_id = request.args.get('sub_id')
        cancel_subscriber = get_cancel_sub(sub_id=sub_id)
        if cancel_subscriber is not None:
            return jsonify(cancel_subscriber.to_dict())
        return '', 404

    elif request.method == 'POST':  # cancel subscriber post method(create)
        name = request.form.get('name')
        mobile_number = request.form.get('mobile')
        address = request.form.get('address')
        photo = request.form.get('photo')
        lat = request.form.get('lat')
        long = request.form.get('long')
        email = request.form.get('email')
        pet_name = request.form.get('pet_name')
        pet_breed = request.form.get('pet_breed')
        package = request.form.get('package')
        sub_type = request.form.get('sub_type')
        price = request.form.get('price')
        product = request.form.get('product')
        start_date = request.form.get('start_date')
        # end_date = request.form.get('end_date')
        cancelsubscriber = create_cancel_sub(name=name, mobile_number=mobile_number, address=address, lat=lat,
                                             long=long, photo=photo,
                                             email=email, pet_name=pet_name, pet_breed=pet_breed, package=package,
                                             sub_type=sub_type, price=price, product=product, start_date=start_date)
        if cancelsubscriber is not None:
            return jsonify(cancelsubscriber.to_dict())
        else:
            return '', 403

    elif request.method == 'PUT':  # put for cancelsubscriptions(update)
        sub_id = request.form.get('sub_id')
        name = request.form.get('name')
        mobile_number = request.form.get('mobile')
        address = request.form.get('address')
        email = request.form.get('email')
        photo = request.form.get('photo')
        lat = request.form.get('lat')
        long = request.form.get('long')
        pet_name = request.form.get('pet_name')
        pet_breed = request.form.get('pet_breed')
        package = request.form.get('package')
        sub_type = request.form.get('sub_type')
        price = request.form.get('price')
        product = request.form.get('product')
        start_date = request.form.get('start_date')
        # end_date = request.form.get('end_date')
        is_updated = update_cancel_sub(sub_id=sub_id, name=name, mobile_number=mobile_number, address=address,
                                       email=email, photo=photo, lat=lat, long=long, pet_name=pet_name,
                                       pet_breed=pet_breed,
                                       package=package,
                                       sub_type=sub_type, price=price, product=product, start_date=start_date)
        if is_updated:
            return '', 204
        else:
            return '', 400

    elif request.method == 'DELETE':
        sub_id = request.form.get('sub_id')
        is_deleted = delete_cancel_sub(sub_id=sub_id)
        if is_deleted:
            return '', 204
        else:
            return '', 400


@subscriber_bp.route("/subscriber/pauses", methods=['GET'])
def get_all_pause_sub():  # get method for agent request
    if request.method == 'GET':
        pause_subs = get_pause_sub(sub_id=None)
        if pause_subs is not None:
            if isinstance(pause_subs, list):
                return jsonify([pause_sub.to_dict() for pause_sub in pause_subs])
            return jsonify(pause_subs.to_dict())
        return '', 404


@subscriber_bp.route("/subscriber/pause", methods=['GET', 'POST', 'PUT', 'DELETE'])
def get_or_modify_pause_sub():  # get method for pause
    if request.method == 'GET':
        sub_id = request.args.get('sub_id')
        pause_subscriber = get_subscriber(sub_id=sub_id)
        if pause_subscriber is not None:
            return jsonify(pause_subscriber.to_dict())
        return '', 404

    elif request.method == 'POST':  # agent post method(create)
        name = request.form.get('name')
        mobile_number = request.form.get('mobile')
        address = request.form.get('address')
        photo = request.form.get('photo')
        lat = request.form.get('lat')
        long = request.form.get('long')
        email = request.form.get('email')
        pet_name = request.form.get('pet_name')
        pet_breed = request.form.get('pet_breed')
        package = request.form.get('package')
        sub_type = request.form.get('sub_type')
        price = request.form.get('price')
        product = request.form.get('product')
        start_date = request.form.get('start_date')
        #end_date = request.form.get('end_date')
        pause_subscriber = create_pause_sub(name=name, mobile_number=mobile_number, address=address,photo=photo, lat=lat, long=long,
                                            email=email, pet_name=pet_name, pet_breed=pet_breed, package=package,
                                            sub_type=sub_type, price=price, product=product, start_date=start_date)
        if pause_subscriber is not None:
            return jsonify(pause_subscriber.to_dict())
        else:
            return '', 403

    elif request.method == 'PUT':  # put for pause subscriptions(update)
        sub_id = request.form.get('sub_id')
        name = request.form.get('name')
        mobile_number = request.form.get('mobile')
        address = request.form.get('address')
        photo = request.form.get('photo')
        email = request.form.get('email')
        lat = request.form.get('lat')
        long = request.form.get('long')
        pet_name = request.form.get('pet_name')
        pet_breed = request.form.get('pet_breed')
        package = request.form.get('package')
        sub_type = request.form.get('sub_type')
        price = request.form.get('price')
        product = request.form.get('product')
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')
        is_updated = update_pause_sub(sub_id=sub_id, name=name, mobile_number=mobile_number, address=address,
                                      email=email,photo=photo,
                                      lat=lat, long=long, pet_name=pet_name, pet_breed=pet_breed, package=package,
                                      sub_type=sub_type, price=price, product=product, start_date=start_date,
                                      end_date=end_date)
        if is_updated:
            return '', 204
        else:
            return '', 400

    elif request.method == 'DELETE':
        sub_id = request.form.get('sub_id')
        is_deleted = delete_pause_sub(sub_id=sub_id)
        if is_deleted:
            return '', 204
        else:
            return '', 400


@subscriber_bp.route("/subscriber/cart", methods=['GET', 'POST', 'PUT'])
def get_or_modify_cart():  # get method for pause
    if request.method == 'GET':
        sub_id = request.args.get('sub_id')
        cart = get_cart(sub_id=sub_id)
        if cart is not None:
            if not isinstance(cart, list):
                return jsonify(cart.to_dict())
            else:
                if len(cart) > 0:
                    return jsonify([cart_item.to_dict() for cart_item in cart])
                else:
                    return '', 404
        return '', 404

    elif request.method == 'POST':  # post method for my order
        sub_id = request.form.get('sub_id')
        product = request.form.get('product')
        price = request.form.get('price')
        quantity = request.form.get('quantity')
        payment_id = request.form.get('payment_id')
        cart = create_cart(sub_id=sub_id, product=product, price=price,
                           quantity=quantity, payment_id=payment_id)
        if cart is not None:
            return jsonify(cart.to_dict())
        else:
            return '', 403

    elif request.method == 'PUT':  # put method for  my orders
        order_id = request.form.get('order_id')
        sub_id = request.form.get('sub_id')
        product = request.form.get('product')
        price = request.form.get('price')
        quantity = request.form.get('quantity')
        payment_id = request.form.get('payment_id')
        is_updated = update_cart(order_id=order_id, sub_id=sub_id, product=product, price=price, quantity=quantity,
                                 payment_id=payment_id)
        if is_updated:
            return '', 204
        else:
            return '', 400


@subscriber_bp.route("/subscriber/checkout", methods=['GET', 'POST', 'PUT'])
def get_or_modify_checkout():  # get method for pause
    if request.method == 'GET':
        order_id = request.args.get('order_id')
        checkout = get_checkout(order_id=order_id)
        if checkout is not None:
            return jsonify(checkout.to_dict())
        return '', 404

    elif request.method == 'POST':  # post method for my order
        sub_id = request.form.get('sub_id')
        product = request.form.get('product')
        price = request.form.get('price')
        quantity = request.form.get('quantity')
        payment_id = request.form.get('payment_id')
        checkout = create_checkout(sub_id=sub_id, product=product, price=price,
                                   quantity=quantity, payment_id=payment_id)
        if checkout is not None:
            return jsonify(checkout.to_dict())
        else:
            return '', 403

    elif request.method == 'PUT':  # put method for  my orders
        order_id = request.form.get('order_id')
        sub_id = request.form.get('sub_id')
        product = request.form.get('product')
        price = request.form.get('price')
        quantity = request.form.get('quantity')
        payment_id = request.form.get('payment_id')
        is_updated = update_checkout(order_id=order_id, sub_id=sub_id, product=product, price=price, quantity=quantity,
                                     payment_id=payment_id)
        if is_updated:
            return '', 204
        else:
            return '', 400
