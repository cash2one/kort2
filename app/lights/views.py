from app.app_and_db import app
from app.lights.forms import LightsForm
from app.lights.constants import *
from flask import abort, Blueprint, flash, render_template, redirect, url_for
from secrets import access_token, device
from time import sleep

import requests
import datetime
domain = "https://api.particle.io/v1/devices/{0}/{1}"

lights = Blueprint('lights', __name__, template_folder='templates/lights')

@lights.route('/', methods=('GET', 'POST'))
def index():
  form = LightsForm()
  if form.validate_on_submit():
    if form.type.data == "rainbow":
      send_request(['1'], "animation")
      return render_template('lights/index.html', form=form)
    if form.type.data == "illinois":
      send_request(['2'], "animation")
      return render_template('lights/index.html', form=form)
    colors = []
    for field in form:
      if 'light' in field.name:
        if len(field.data) > 0:
          colors.append(str(field.data).replace("#", ""))
        else: 
          break
    delay = 0
    if form.delay.data.isdigit():
      delay = form.delay.data
    else:
      light_strip(colors)
    if form.type.data == "forwards":
      light_strip_forwards(colors, delay)
    else:
      light_strip_backwards(colors, delay)
  return render_template('lights/index.html', form=form)

def light_strip(colors):
  return send_request(colors, "color")

def clear_strip():
  return send_request([black], "color")

def light_strip_forwards(colors, delay):
    return send_request([str(delay)] + colors, "forwards")  

def light_strip_backwards(colors, delay):
    return send_request([str(delay)] + colors, "backwards")

def send_request(colors, endpoint):
  payload = {'access_token' : access_token, 'args' : ",".join(colors)}
  response = requests.post(get_url(endpoint), data = payload)
  print str(datetime.datetime.now()) + "\t : \t" + str(payload)
  print str(datetime.datetime.now()) + "\t : \t" + response.text


def get_url(endpoint):
  if endpoint not in ['color', 'forwards', 'backwards', 'animation']:
    raise NameError(str(endpoint) + " is not a valid endpoint")
  return domain.format(device, endpoint);

app.register_blueprint(lights, url_prefix='/lights')