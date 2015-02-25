from app import app
from flask import render_template, request, redirect, url_for, flash, jsonify, session
import os
from werkzeug import secure_filename
from flask_wtf.file import FileField
import json
import demjson
from .forms import Profiler
from db_insert import *
from . import db, models
import time


@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html', title="Home")

@app.route('/viewprofile')
def viewprofile():
  a = models.Profile.query.get(1)
  return render_template('profiler3.html', userid= str(a.userid), fname=str(a.fname), lname=str(a.lname), username=str(a.username), sex=str(a.sex), age=str(a.age), highscore=str(a.highscore), tdollar=str(a.tdollar), profile_add_on=str(a.profile_add_on), pic=os.path.join(os.path.abspath(os.path.dirname('imagez')),str(a.image)))

#create new profile
@app.route('/profile', methods=['POST', 'GET'])
def profile():
  form = Profiler()
  if form.validate()==True and request.method == 'POST':
    filename = secure_filename(form.image.data.filename)
    form.image.data.save(os.path.join(os.path.abspath(os.path.dirname('imagez')),filename))
    #form = Profilers(request.form)
    insert(form.fname.data, form.lname.data, form.username.data, form.sex.data, form.age.data, filename, 0, 0)
    
    flash('%s\'s login was successful' % form.username.data)
    return redirect(url_for('index'))
    
  return render_template('profiler1.html', title='Sign Up', form=form)


#list of profiles
@app.route('/profiles', methods=['POST', 'GET'])
def profiles():
  u = models.Profile.query.all()
  lst=[]
  
  for i in u: 
    dic = {'username':i.username, 'userid':i.userid}
    lst += [dic]
    
  usr = {'users':lst}
  return jsonify(usr)
   

#view a profile
@app.route('/profile/<userid>', methods=['GET', 'POST'])
def profileView(userid):
  u = models.Profile.query.filter_by(userid=userid).first_or_404()
  
  return jsonify({
                  'userid':u.userid, 
                  'username':u.username, 
                  'sex':u.sex, 
                  'age':u.age, 
                  'highscore':u.highscore, 
                  'tdollar':u.tdollar,
                  'profile_add_on':u.profile_add_on,
                  'image':u.image
                 })

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html', title='404'), 404

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=8080)