from flask import Flask
from app.config import Configuration
from app.routes import orders
from app.routes import session
from .models import db, Employee
from flask_login import LoginManager

app = Flask(__name__) # declare the app
app.config.from_object(Configuration) # Use the configuration class for config

app.register_blueprint(orders.bp) # register the blueprint defined in orders.py
app.register_blueprint(session.bp) # register the blueprint defined in session.py

db.init_app(app) # Configure the app with SQLAlchemy

# init_app() method is used to configure the app for larger apps

login = LoginManager(app)
login.login_view = "session.login"


@login.user_loader
def load_user(id):
    return Employee.query.get(int(id))