from flask import render_template, flash, session, request, redirect, url_for
from app.app_and_db import app
from app.utility.robot import requires_human
from app.contact.forms import ContactForm

@app.route('/contact', methods=('GET', 'POST'))
@requires_human
def contact():
  form = ContactForm()
  if form.validate_on_submit():
    flash("Your email has been passed along!", "success")
    return redirect(url_for('index'))
  return render_template('pages/contact.html', form = form)