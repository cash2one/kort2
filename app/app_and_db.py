from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.ext.assets import Environment

app = Flask(__name__)
db = SQLAlchemy(app)
webassets = Environment(app)