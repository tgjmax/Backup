from flask import Blueprint, request, jsonify

agent_bp = Blueprint('agent_bp', __name__,
                     template_folder='templates')

from agent.helpers import create_agent, update_agent, get_agent, create_request, update_request, \
    create_earnings, update_earnings, get_earnings, get_request, get_agent_requests


@agent_bp.route("/agents", methods=['GET'])
def get_all_agents():  # get method for all agents
    if request.method == 'GET':
        agents = get_agent()
        if agents is not None:
            return jsonify([agent.to_dict() for agent in agents])
        return '', 404


@agent_bp.route("/login/agent/<string:mobile_number>", methods=["GET"])
def login_agent(mobile_number):
    agent = get_agent(mobile_number=mobile_number)
    return jsonify(agent.to_dict())


@agent_bp.route("/agent/", methods=['GET', 'POST', 'PUT'])
def get_or_modify_agent():  # get method for agent
    if request.method == 'GET':
        id = request.args.get('id')
        agent = get_agent(id=id)
        if agent is not None:
            return jsonify(agent.to_dict())
        return '', 404

    elif request.method == 'POST':  # agent post method(create)
        name = request.form.get('name')
        mobile_number = request.form.get('mobile')
        address = request.form.get('address')
        business_name = request.form.get('business_name')
        photo = request.form.get('photo')
        email = request.form.get('email')
        type = request.form.get('type')
        agent = create_agent(name=name, mobile_number=mobile_number, address=address, business_name=business_name,
                             email=email, photo=photo, type=type)
        if agent is not None:
            return jsonify(agent.to_dict())
        else:
            return '', 403

    elif request.method == 'PUT':  # put for agent(update)
        id = request.form.get('id')
        name = request.form.get('name')
        mobile_number = request.form.get('mobile')
        address = request.form.get('address')
        business_name = request.form.get('business_name')
        email = request.form.get('email')
        photo = request.form.get('photo')
        type = request.form.get('type')
        is_updated = update_agent(id=id, name=name, mobile_number=mobile_number, address=address,
                                  business_name=business_name,
                                  email=email, photo=photo, type=type)
        if is_updated:
            return '', 204
        else:
            return '', 400


@agent_bp.route("/agent/requests", methods=['GET'])
def get_all_agent_requests():  # get method for all agents
    if request.method == 'GET':
        agent_id = request.args.get('agent_id')
        agent_requests = get_agent_requests(agent_id=agent_id)
        if agent_requests is not None:
            return jsonify([agent_request.to_dict() for agent_request in agent_requests])
        return '', 404


@agent_bp.route("/agent/request/", methods=['GET', 'POST', 'PUT'])
def get_or_modify_request():  # get method for agent request
    if request.method == 'GET':
        request_id = request.args.get('request_id')
        customer_number = request.args.get('customer_number')
        agent_request = get_request(request_id=request_id, customer_number=customer_number)
        if request is not None:
            return jsonify(agent_request.to_dict())
        return '', 404

    elif request.method == 'POST':  # post method for agent_request
        product_id = request.form.get('product_id')
        customer_name = request.form.get('customer_name')
        customer_number = request.form.get('customer_number')
        customer_address = request.form.get('customer_address')
        customer_email = request.form.get('customer_email')
        quantity = request.form.get('quantity')
        agent_request = create_request(product_id=product_id, customer_name=customer_name,
                                       customer_number=customer_number, customer_address=customer_address,
                                       customer_email=customer_email, quantity=quantity)
        if agent_request is not None:
            return jsonify(agent_request.to_dict())
        else:
            return '', 403

    elif request.method == 'PUT':  # put method for agent_request
        request_id = request.form.get('request_id')
        product_id = request.form.get('product_id')
        customer_name = request.form.get('customer_name')
        customer_number = request.form.get('customer_number')
        customer_address = request.form.get('customer_address')
        customer_email = request.form.get('customer_email')
        quantity = request.form.get('quantity')
        is_updated = update_request(request_id=request_id, product_id=product_id, customer_name=customer_name,
                                    customer_number=customer_number, customer_address=customer_address,
                                    customer_email=customer_email, quantity=quantity)
        if is_updated:
            return '', 204
        else:
            return '', 400


@agent_bp.route("/agent/earnings/", methods=['GET', 'POST', 'PUT'])
def get_or_earnings():  # get method for earnings
    if request.method == 'GET':
        id = request.args.get('id')
        earnings = get_earnings(id=id)
        if earnings is not None:
            return jsonify(earnings.to_dict())
        return '', 404

    elif request.method == 'POST':  # post meothod for earnings
        date = request.form.get('date')
        time = request.form.get('time')
        product_id = request.form.get('product_id')
        request_id = request.form.get('request_id')
        price = request.form.get('price')
        earn = request.form.get('earn')
        earnings = create_earnings(date=date, time=time, product_id=product_id, request_id=request_id, price=price,
                                   earn=earn)
        if earnings is not None:
            return jsonify(earnings.to_dict())
        else:
            return '', 403

    elif request.method == 'PUT':  # put method for  earnings
        id = request.form.get('id')
        date = request.form.get('date')
        time = request.form.get('time')
        product_id = request.form.get('product_id')
        request_id = request.form.get('request_id')
        price = request.form.get('price')
        earn = request.form.get('earn')
        is_updated = update_earnings(id=id, date=date, time=time, product_id=product_id, request_id=request_id,
                                     price=price, earn=earn)
        if is_updated:
            return '', 204
        else:
            return '', 400
