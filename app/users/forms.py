from flask_security.forms import RegisterForm
from wtforms import StringField, validators

class ExtendedRegisterForm(RegisterForm):
  first_name = StringField('First Name', [validators.Required()])
  last_name = StringField('Last Name', [validators.Required()])
