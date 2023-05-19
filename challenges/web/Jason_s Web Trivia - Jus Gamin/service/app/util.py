import jwt, datetime
from flask import request, redirect
from functools import wraps

from database import database

def createJWT(username):
  expires = datetime.datetime.utcnow() + datetime.timedelta(hours=1)

  encoded = jwt.encode(
    {
      "username": username,
      "exp": expires
    },
    key=None,
    algorithm=None
  )

  return encoded

def decodeJWT(token):
  if not token.endswith("."):
    # For some reason pyJWT needs the token to end with a period if it's not signed
    token += "."

  data = jwt.decode(token, options={"verify_signature": False})
  return data
  

def isAuthenticated(f):
  @wraps(f)
  def decorated_function(*args, **kwargs):
    token = request.cookies.get("token")

    if token is None:
      return redirect("/login")
    
    if not token.endswith("."):
      # For some reason pyJWT needs the token to end with a period if it's not signed
      token += "."

    try:
      data = jwt.decode(token, options={"verify_signature": False, "verify_exp": True})
    except jwt.ExpiredSignatureError:
      return redirect("/login")
    except jwt.InvalidTokenError:
      return {"error": "Invalid token"}, 401
    
    # Check if user exists
    username = data["username"]
    user_id = database.get_user(username)
    if not user_id:
      # If user not found, delete the cookie and redirect to login
      response = redirect("/login")
      response.set_cookie("token", "", expires=0)
      return response

    return f(*args, **kwargs)
  
  return decorated_function