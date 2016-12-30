from app.app_and_db import app
from app.utility.forms import RecaptchaForm
from datetime import datetime, timedelta
from flask import flash, session, redirect, render_template, request, url_for
from functools import wraps

IS_HUMAN_COOKIE_KEY = "is_human"
IS_HUMAN_COOKIE_VALUE = "yes"

@app.route('/robot', methods=('GET', 'POST'))
def robot():
  form = RecaptchaForm(redirect=request.args.get('next', ''))
  if form.validate_on_submit():
    flash("Thanks for verifying that you're not a robot!", 'success')
    response = None
    if form.redirect.data and len(form.redirect.data) > 0:
      response = app.make_response(redirect(form.redirect.data))
    else: 
      response = app.make_response(redirect(url_for('index')))
    expire_date = datetime.now()
    expire_date = expire_date + timedelta(days=365)
    response.set_cookie(IS_HUMAN_COOKIE_KEY, IS_HUMAN_COOKIE_VALUE, expires=expire_date)
    return response
  return render_template('pages/robot.html', form=form)

def requires_human(f):
  @wraps(f)
  def decorated_function(*args, **kwargs):
    is_human = request.cookies.get(IS_HUMAN_COOKIE_KEY)
    if is_human == IS_HUMAN_COOKIE_VALUE:
      return f(*args, **kwargs)
    return redirect(url_for('robot', next=request.url))
  return decorated_function