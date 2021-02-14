# from flask import Blueprint, request, jsonify
#
# flask_app_bp = Blueprint('flask_app_bp', __name__,
#                          template_folder='templates')
#
# from helpers import get_delivery_agent, update_delivery_agent, create_delivery_agent, get_subscriber, \
#     create_subscriber, update_subscriber
#
#
# @flask_app_bp.route("/delivery/", methods=['GET', 'POST', 'PUT'])
# def get_or_modify_delivery_agent():
#     if request.method == 'GET':
#         pin = request.args.get('pin')
#         did = request.args.get('did')
#         delivery_agent = get_delivery_agent(pin=pin, did=did)
#         print(type(delivery_agent))
#         if delivery_agent is not None:
#             if isinstance(delivery_agent, list):
#                 return jsonify([agent.to_dict() for agent in delivery_agent])
#             else:
#                 return jsonify(delivery_agent.to_dict())
#         return '', 404
#
#     elif request.method == 'POST':
#         name = request.form.get('name')
#         mobile = request.form.get('mobile')
#         email = request.form.get('email')
#         photo = request.form.get('photo')
#         delivery_agent = create_delivery_agent(name=name, mobile=mobile, email=email, photo=photo, pin=None)
#         if delivery_agent is not None:
#             return jsonify(delivery_agent.to_dict())
#         else:
#             return '', 403
#
#     elif request.method == 'PUT':
#         did = request.form.get('did')
#         name = request.form.get('name')
#         mobile = request.form.get('mobile')
#         email = request.form.get('email')
#         photo = request.form.get('photo')
#         is_updated = update_delivery_agent(did=did, name=name, mobile=mobile, email=email, photo=photo)
#         if is_updated:
#             return '', 204
#         else:
#             return '', 400
#
#
# @flask_app_bp.route("/subscriber/", methods=['GET', 'POST', 'PUT'])
# def get_or_modify_subscriber():
#
#     if request.method == 'GET':
#         sid = request.args.get('sid')
#         subscriber = get_subscriber(sid=sid)
#         if subscriber is not None:
#             if isinstance(subscriber, list):
#                 return jsonify([sub.to_dict() for sub in subscriber])
#             else:
#                 return jsonify(subscriber.to_dict())
#         return '', 404
#
#     elif request.method == 'POST':
#         name = request.form.get('name')
#         mobile = request.form.get('mobile')
#         address = request.form.get('address')
#         latitude = request.form.get('latitude')
#         longitude = request.form.get('longitude')
#         email = request.form.get('email')
#         pet_name = request.form.get('pet_name')
#         pet_breed = request.form.get('pet_breed')
#         pet_age = request.form.get('pet_age')
#         subscriber = create_subscriber(sname=name, smobile=mobile, semail=email, saddress=address, slat=latitude,
#                                        slong=longitude, pet_name=pet_name, pet_breed=pet_breed, pet_age=pet_age)
#         if subscriber is not None:
#             return jsonify(subscriber.to_dict())
#         else:
#             return '', 403
#
#     elif request.method == 'PUT':
#         sid = request.form.get('sid')
#         name = request.form.get('name')
#         mobile = request.form.get('mobile')
#         address = request.form.get('address')
#         latitude = request.form.get('latitude')
#         longitude = request.form.get('longitude')
#         email = request.form.get('email')
#         pet_name = request.form.get('pet_name')
#         pet_breed = request.form.get('pet_breed')
#         pet_age = request.form.get('pet_age')
#         is_updated = update_subscriber(sid=sid, sname=name, smobile=mobile, semail=email, saddress=address,
#                                        slat=latitude,
#                                        slong=longitude, pet_name=pet_name, pet_breed=pet_breed, pet_age=pet_age)
#         if is_updated:
#             return '', 204
#         else:
#             return '', 400
