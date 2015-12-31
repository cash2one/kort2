from flask import render_template, redirect, url_for
from app.app_and_db import app
from app.utility.robot import requires_human

@app.route('/')
@app.route('/index')
def index():
  return render_template('pages/home_page.html')

@app.route('/resume')
@requires_human
def resume():
  return render_template('pages/resume.html')

@app.errorhandler(403)
def is403(e):
  return render_template('base_templates/error.html', e = e)

@app.errorhandler(404)
def is404(e):
  return render_template('base_templates/error.html', e = "Oops, you shouldn't have ended up here!")

@app.errorhandler(500)
def is500(e):
  return str(e)#render_template('base_templates/error.html', e = e)