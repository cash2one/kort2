from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.ext.assets import Environment
from flask_mail import Mail

app = Flask(__name__)
app.config.from_object('app.startup.settings')
db = SQLAlchemy(app)

webassets = Environment(app)
mail = Mail(app)

from app.startup import assets

#views
from app.admin import views
from app.articles import views
from app.contact import views
from app.pages import views