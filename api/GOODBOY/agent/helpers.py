from agent.models import Agent, Request, Earnings
from main import db


def create_agent(name, mobile_number, address, business_name, photo, email, type):  #
    db.create_all()
    agent = Agent(name=name, mobile_number=mobile_number, address=address, business_name=business_name, photo=photo,
                  email=email,
                  type=type)
    try:
        db.create_all()
        db.session.add(agent)
        db.session.commit()
        return agent

        from pathlib import Path  # file uploading for agent
        agent.photo = upload_file(
            '{}/PycharmProjects/GOODBOY/uploads/agents/{}/'.format(str(Path.home()), agent.id),
            file=photo, type='agent', id=agent.id)
        db.session.add(subscriber)
        db.session.commit()
        return agent

    except Exception as e:
        db.session.rollback()
        print(e)
        return None


def create_request(product_id, customer_name, customer_number, customer_address, customer_email, quantity):
    db.create_all()
    request = Request(product_id=product_id, customer_name=customer_name,
                      customer_number=customer_number, customer_address=customer_address, customer_email=customer_email,
                      quantity=quantity)
    try:
        db.create_all()
        db.session.add(request)
        db.session.commit()
        return request
    except Exception as e:
        db.session.rollback()
        print(e)
        return None


def create_earnings(date, time, product_id, request_id, price, earnings):
    db.create_all()
    agent = Earnings(date=date, time=time, product_id=product_id, request_id=request_id, price=price, earnings=earnings)
    try:
        db.create_all()
        db.session.add(agent)
        db.session.commit()
        return agent
    except Exception as e:
        db.session.rollback()
        print(e)
        return None


def get_agent(id=None, mobile_number=None):
    db.create_all()
    if id is None and mobile_number is None:
        return None
    elif id is not None:
        return Agent.query.get(id)
    elif mobile_number is not None:
        return Agent.query.filter_by(mobile_number=mobile_number).first()


def get_agent_requests(agent_id):
    db.create_all()
    return Request.query.filter_by(agent_id=agent_id).first()


def get_request(request_id=None, customer_number=None):
    db.create_all()
    if request_id is None and customer_number is None:
        return Request.query.all()
    elif customer_number is None:
        return Request.query.filter_by(request_id=request_id).first()
    else:
        return Request.quert.filer_by(customer_number=customer_number).first()


def get_earnings(id=None):
    db.create_all()
    if id is None:
        return Earnings.query.all()
    else:
        return Earnings.query.filter_by(id=id).first()


def update_agent(id, name, mobile_number, address, business_name, photo, email, type):
    agent = get_agent(id=id)
    if agent is not None:
        if name is not None:
            agent.name = name
        if mobile_number is not None:
            agent.mobile_number = mobile_number
        if address is not None:
            agent.address = address
        if business_name is not None:
            agent.business_name = business_name
        if photo is not None:
            agent.photo = photo
        if email is not None:
            agent.email = email
        if type is not None:
            agent.type = type
        try:
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            db.session.rollback()
            return False
    else:
        return False


def update_request(request_id, product_id, customer_name, customer_number, customer_address, customer_email, quantity):
    request = get_request(request_id=request_id)
    if request is not None:
        request.product_id = product_id
        request.customer_name = customer_name
        request.customer_number = customer_number
        request.customer_address = customer_address
        request.customer_email = customer_email
        request.quantity = quantity
        try:
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            db.session.rollback()
            return False
    else:
        return False


def update_earnings(id, date, time, product_id, request_id, price, earn):
    earnings = get_earnings(id=id)
    if earnings is not None:
        earnings.date = date
        earnings.time = time
        earnings.product_id = product_id
        earnings.request_id = request_id
        earnings.price = price
        earnings.earnings = earn
        try:
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            db.session.rollback()
            return False
    else:
        return False
