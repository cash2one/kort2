from app.app_and_db import app
from flask import Blueprint, jsonify, render_template

import datetime
import random
import requests

dashboard = Blueprint('dashboard', __name__)

cumtd_endpoint = 'https://developer.cumtd.com/api/{0}/{1}/{2}'
cumtd_endpoint = cumtd_endpoint.format('v2.2', 'json', 'GetDeparturesByStop')

wunderground_endpoint = 'http://api.wunderground.com/api/{0}/hourly/q/{1}/{2}.json'
wunderground_endpoint = wunderground_endpoint.format(app.config['WUNDERGROUND_API_KEY'], 'IL', 'Champaign')

@dashboard.route('/')
def index():
  time=datetime.datetime.now().time().strftime('%I:%M').lstrip('0')
  return render_template('pages/dashboard.html', image_number=random.randrange(1, 9), time=time)

#Query no more than once a minute
@dashboard.route('/bus')
def bus_schedule():
  params = {'key' : app.config['CUMTD_API_KEY'],
            'stop_id' : 'GRN4TH',
            'count' : '5'}
  response = requests.get(cumtd_endpoint, params=params)
  json = response.json()
  departures = []
  for departure in json['departures'] :
    if departure['trip']['direction'] == 'East':
      departures.append(departure)
  return jsonify(departures=departures)

#Query no more than once every three minutes
@dashboard.route('/weather')
def weather():
  response = requests.get(wunderground_endpoint)
  json = response.json()
  return jsonify(json)

app.register_blueprint(dashboard, url_prefix='/dashboard')