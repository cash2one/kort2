from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.ext.assets import Environment
from flask.ext.security import Security, SQLAlchemyUserDatastore
from flask_mail import Mail

app = Flask(__name__)
app.config.from_object('app.startup.settings')
db = SQLAlchemy(app)

webassets = Environment(app)
mail = Mail(app)

from app.users.models import Role, User
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

from app.startup import assets

#views
from app.admin import views
from app.articles import views
from app.contact import views
from app.dashboard import views
from app.pages import views