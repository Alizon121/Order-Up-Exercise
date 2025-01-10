from flask import Flask
from app.config import Configuration
from app.routes import orders

app = Flask(__name__) # declare the app
app.config.from_object(Configuration) # Use the configuration class for config
app.register_blueprint(orders.bp) # register the blueprint defined in orders.py