from app.app_and_db import app, mail
from flask.ext.mail import Message

def send_email(subject, recipients, html_body):
  msg = Message(subject, sender=app.config['MAIL_USERNAME'], recipients=recipients)
  msg.html = html_body
  mail.send(msg)