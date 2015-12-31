from app.app_and_db import app
from app.utility.forms import RecaptchaForm
from flask import flash, session, redirect, render_template, request, url_for
from functools import wraps

@app.route('/robot', methods=('GET', 'POST'))
def robot():
  form = RecaptchaForm(redirect=request.args.get('next', ''))
  if form.validate_on_submit():
    flash("Thanks for verifying that you're not a robot!", 'success')
    session['human'] = True
    if form.redirect.data and len(form.redirect.data) > 0:
      return redirect(form.redirect.data)
    else: 
      return redirect(url_for('index'))
  return render_template('pages/robot.html', form=form)

def requires_human(f):
  @wraps(f)
  def decorated_function(*args, **kwargs):
    if 'human' in session and session['human'] is True:
      return f(*args, **kwargs)
    return redirect(url_for('robot', next=request.url))
  return decorated_function