from app.app_and_db import app
from flask import jsonify, render_template, request
from flask.ext import admin
from flask_security.decorators import roles_accepted
from werkzeug import secure_filename

import os

@app.route('/admin/upload', methods=('GET', 'POST'))
def admin():
  file = request.files['upload']
  if file:
    filename = secure_filename(file.filename)
    path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(path):
      response = {
      'uploaded': 0,
      'error': {
        'message': 'File name already taken. Please rename.'
        }
      }
      return jsonify(response), 403
    file.save(path)
    response = {
      'uploaded': 1,
      'url': 'http://files.nickkortendick.com/' + filename,
      'fileName' : filename
    }
    return jsonify(response), 201
  else: 
    response = {
      'uploaded': 0,
      'error': {
        'message': 'No file was attached'
        }
      }
    return jsonify(response), 501