from flask_wtf import Form, RecaptchaField
from wtforms import SubmitField, StringField, TextAreaField, validators
from wtforms.fields.html5 import EmailField

class ContactForm(Form):
  name = StringField("Name",  [validators.InputRequired("Please enter your name.")])
  email = EmailField('Email address', [validators.DataRequired(), validators.Email()])
  subject = StringField("Subject",  [validators.InputRequired("Please enter a subject.")])
  message = TextAreaField("Message",  [validators.InputRequired("Please include your message")])
  submit = SubmitField("Send")