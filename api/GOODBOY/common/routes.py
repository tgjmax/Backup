from flask import Blueprint, request, jsonify

common_bp = Blueprint('common_bp', __name__,
                      template_folder='templates')

from common.helpers import get_sample_request, create_sample_request, update_sample_request, delete_sample_request, \
    get_menus, create_menus, update_menus


@common_bp.route("/samples", methods=['GET'])
def get_all_sample_request():  # get method for all agents
    if request.method == 'GET':
        sample_requests = get_sample_request()
        if sample_requests is not None:
            return jsonify([sample_request.to_dict() for sample_request in sample_requests])
        return '', 404


@common_bp.route("/sample_request/", methods=['GET', 'POST', 'PUT', 'DELETE'])
def get_or_modify_sample_request():  # get method for sample request
    if request.method == 'GET':
        sample_id = request.args.get('sample_id')
        sample_request = get_sample_request(sample_id=sample_id)
        if sample_request is not None:
            return jsonify(sample_request.to_dict())
        return '', 404

    elif request.method == 'POST':  # sample request post method(create)
        customer_name = request.form.get('customer_name')
        customer_number = request.form.get('customer_number')
        customer_address = request.form.get('customer_address')
        pet_name = request.form.get('pet_name')
        pet_breed = request.form.get('pet_breed')
        pet_age = request.form.get('pet_age')
        pet_weight = request.form.get('pet_weight')
        sample_request = create_sample_request(customer_name=customer_name, customer_number=customer_number,
                                               customer_address=customer_address, pet_name=pet_name,
                                               pet_breed=pet_breed, pet_age=pet_age, pet_weight=pet_weight)
        if sample_request is not None:
            return jsonify(sample_request.to_dict())
        else:
            return '', 403

    elif request.method == 'PUT':  # put for sample request(update)
        sample_id = request.form.get('sample_id')
        customer_name = request.form.get('customer_name')
        customer_number = request.form.get('customer_number')
        customer_address = request.form.get('customer_address')
        pet_name = request.form.get('pet_name')
        pet_breed = request.form.get('pet_breed')
        pet_age = request.form.get('pet_age')
        pet_weight = request.form.get('pet_weight')
        is_updated = update_sample_request(sample_id=sample_id, customer_name=customer_name,
                                           customer_number=customer_number, customer_address=customer_address,
                                           pet_name=pet_name, pet_breed=pet_breed, pet_age=pet_age,
                                           pet_weight=pet_weight)
        if is_updated:
            return '', 204
        else:
            return '', 400

    elif request.method == 'DELETE':
        sample_id = request.form.get('sample_id')
        is_deleted = delete_sample_request(sample_id=sample_id)
        if is_deleted:
            return '', 204
        else:
            return '', 400


@common_bp.route("/menus", methods=['GET'])
def get_all_menus():  # get method for all menus list
    if request.method == 'GET':
        menus = get_menus()
        if menus is not None:
            return jsonify([menu.to_dict() for menu in menus])
        return '', 404


@common_bp.route("/menu", methods=['GET', 'POST', 'PUT'])
def get_or_modify_menu():  # get method for menu based on id
    if request.method == 'GET':
        product_id = request.args.get('product_id')   #getting values based pn product id
        menu = get_menus(product_id=product_id)
        if menu is not None:
            return jsonify(menu.to_dict())
        return '', 404

    elif request.method == 'POST':  # menu post method(create)
        product_name = request.form.get('product_name')
        net_weight = request.form.get('net_weight')
        price = request.form.get('price')
        brand = request.form.get('brand')
        product_for = request.form.get('product_for')
        product_description = request.form.get('product_description')
        product_image = request.form.get('product_image')
        product_type = request.form.get('product_type')
        menu = create_menus(product_name=product_name, net_weight=net_weight,
                            price=price, brand=brand,
                            product_for=product_for, product_description=product_description,
                            product_image=product_image, product_type=product_type)
        if menu is not None:
            return jsonify(menu.to_dict())
        else:
            return '', 403

    elif request.method == 'PUT':  # put for menu(update)
        product_id = request.form.get('product_id')
        product_name = request.form.get('product_name')
        net_weight = request.form.get('net_weight')
        price = request.form.get('price')
        brand = request.form.get('brand')
        product_for = request.form.get('product_for')
        product_description = request.form.get('product_description')
        product_image = request.form.get('product_image')
        product_type = request.form.get('product_type')
        is_updated = update_menus(product_id=product_id, product_name=product_name,
                                           net_weight=net_weight, price=price,
                                           brand=brand, product_for=product_for, product_description=product_description,
                                           product_image=product_image,product_type=product_type)
        if is_updated:
            return '', 204
        else:
            return '', 400
