from flask import Flask
from app.config import Configuration
from app.routes import orders
from app.routes import session
from app.models import db, Employee
from flask_login import LoginManager

app = Flask(__name__) # declare the app
app.config.from_object(Configuration) # Use the configuration class for config

app.register_blueprint(orders.bp) # register the blueprint defined in orders.py
app.register_blueprint(session.bp) # register the blueprint defined in session.py

db.init_app(app) # Configure the app with SQLAlchemy

# init_app() method is used to configure for larger apps

login = LoginManager(app) #protect the routes
# This allows us to be redirected to the login page
login.login_view = "session.login"


@login.user_loader #gets employee objects form db
def load_user(id):
    return Employee.query.get(int(id))