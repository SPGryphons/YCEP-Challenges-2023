from flask import Blueprint, render_template, request, session, redirect

from database import db
from util import isAuthenticated

flag = open('flag.txt').read()

web = Blueprint('web', __name__)
api = Blueprint('api', __name__)

def anticheat(q):
  blacklist = ['insert','delete','alter','drop','sleep','create','into']
  for i in blacklist:
    if i in q.lower():
      return False 
  else:
    return True

@web.route('/')
def login():
  return render_template('login.html')

@web.route('/logout')
def logout():
  session.clear()
  return redirect('/')

@web.route('/home')
@isAuthenticated
def home():
  return render_template('home.html')

@web.route('/ycep-spoilers-at-this-endpoint')
@isAuthenticated
def spoilers():
  return render_template('ycep.html', flag=flag)

@api.route('/login', methods=['POST'])
def login_api():
  if not request.is_json:
    return "Invalid request", 400
  
  data = request.get_json()
  username = data.get('username', '')
  password = data.get('password', '')

  if not anticheat(username) or not anticheat(password):
    return {"error": "Nice try!"}, 401

  if not username or not password:
    return {"error": "All fields are required!"}, 401
  
  user = db.login(username, password)

  if user:
    session['token'] = user
    return "Logged in successfully!", 200
  
  return {"error": "Incorrect username or password."}, 401