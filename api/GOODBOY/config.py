from models import Delivery, Subscriber
# from main import db


# def get_delivery_agent(aid=aid , aid is None):
#     db.create_all()
#     if aid is None :
#         return Delivery.query.all()
#     else:
#         return Delivery.query.filter_by(aid=aid).first()


# def create_delivery_agent(name, mobile, email, photo, pin):
#     user_delivery_agent = Delivery(name=name, mobile=mobile, email=email, photo=photo, pin=pin)
#     try:
#         db.create_all()
#         db.session.add(user_delivery_agent)
#         db.session.commit()
#         return user_delivery_agent
#     except Exception as e:
#         db.session.rollback()
#         print(e)
#         return None


# def update_delivery_agent(did, name, mobile, email, photo):
#     delivery_agent = get_delivery_agent(did=did, pin=None)
#     if delivery_agent is not None:
#         delivery_agent.name = name
#         delivery_agent.mobile = mobile
#         delivery_agent.email = email
#         delivery_agent.photo = photo
#         try:
#             db.session.commit()
#             return True
#         except Exception as e:
#             print(e)
#             db.session.rollback()
#             return False
#     else:
#         return False


# def get_subscriber(sid):
#     db.create_all()
#     if sid is None:
#         return Subscriber.query.all()
#     return Subscriber.query.filter_by(sid=sid).first()


# def create_subscriber(sname, smobile, semail, saddress, slat, slong, pet_name, pet_breed, pet_age):
#     subscriber = Subscriber(sname=sname, smobile=smobile, semail=semail, saddress=saddress, slat=slat,
#                             slong=slong, pet_name=pet_name, pet_breed=pet_breed, pet_age=pet_age)

#     try:
#         db.create_all()
#         db.session.add(subscriber)
#         db.session.commit()
#         return subscriber

#     except Exception:
#         db.session.rollback()
#         return None


# def update_subscriber(sid, sname, smobile, saddress, semail, slat, slong, pet_name, pet_breed, pet_age):
#     subscriber = get_subscriber(sid=sid)
#     if subscriber is not None:
#         subscriber.name = sname
#         subscriber.mobile = smobile
#         subscriber.address = saddress
#         subscriber.slat = slat
#         subscriber.slong = slong
#         subscriber.email = semail
#         subscriber.pet_name = pet_name
#         subscriber.pet_breed = pet_breed
#         subscriber.pet_age = pet_age
#         try:
#             db.session.commit()
#             return True
#         except Exception as e:
#             print(e)
#             db.session.rollback()
#             return False
#     else:
#         return False

