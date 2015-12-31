from flask_wtf import Form, RecaptchaField
from wtforms import HiddenField

class RecaptchaForm(Form):
  recaptcha = RecaptchaField()
  redirect = HiddenField('redirect')