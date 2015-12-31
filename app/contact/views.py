from app.app_and_db import app, mail
from app.contact.forms import ContactForm
from app.contact.mailer import send_email
from app.utility.robot import requires_human
from flask import render_template, flash, session, request, redirect, url_for
from flask_mail import Message

@app.route('/contact', methods=('GET', 'POST'))
@requires_human
def contact():
  form = ContactForm()
  if form.validate_on_submit():
    send_email(form.subject.data, ["hi@nickkortendick.com"], render_template("emails/contact.html", user=form.name.data, email=form.email.data, message=form.message.data))
    flash("Your email has been passed along!", "success")
    return redirect(url_for('index'))
  return render_template('pages/contact.html', form = form)