from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from routes import news_bp

# Setting up flask app
app = Flask(__name__, static_folder='uploads/')

# Setting up database uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://wielabs:Wielabsdb@123@localhost/witness'

# Registering blueprints
app.register_blueprint(news_bp)

# Setting up SQLAlchemy
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010)
