from app.app_and_db import app
from flask import jsonify, render_template
from flask.ext import admin

@admin.expose('/')
def admin(self):
  return render_template('admin/index.html')

@app.route('/admin/upload', methods=('GET', 'POST'))
def admin():
  #see http://docs.ckeditor.com/#!/guide/dev_file_upload
  response = {
    'uploaded': 0,
    'error': {
        'message': 'Feature not implemented'
    }
  }
  return jsonify(response), 501