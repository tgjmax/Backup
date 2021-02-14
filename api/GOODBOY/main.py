from pathlib import Path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# from flask_bcrypt import Bcrypt


flask_app = Flask(__name__, static_folder='{}/PycharmProjects/GOODBOY/uploads'.format(Path.home()))
flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://wielabs:Wielabsdb@123@localhost/GOODBOY'
flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(flask_app)


def register_blueprints():
    from agent.routes import agent_bp
    from subscriber.routes import subscriber_bp
    from common.routes import common_bp
    flask_app.register_blueprint(agent_bp)
    flask_app.register_blueprint(subscriber_bp)
    flask_app.register_blueprint(common_bp)

if "__main__" == __name__:
    register_blueprints()
    flask_app.run(host='0.0.0.0', debug=True)
