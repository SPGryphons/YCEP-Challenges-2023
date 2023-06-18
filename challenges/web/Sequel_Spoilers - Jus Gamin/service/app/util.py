import jwt, secrets, datetime
from flask import abort, request, redirect, session
from functools import wraps

generate = lambda x: secrets.token_hex(x)

key = generate(50)

def createJWT(username):
  expires = datetime.datetime.utcnow() + datetime.timedelta(hours=1)

  encoded = jwt.encode(
    {
      'username': username,
      'exp': expires
    },
    key,
    algorithm='HS256'
  )

  return encoded

def verifyJWT(token):
  try:
    decoded = jwt.decode(
      token,
      key,
      algorithms=['HS256']
    )

    return decoded
  except jwt.ExpiredSignatureError:
    return redirect('/login')
  except jwt.InvalidTokenError:
    return abort(400, "Invalid token")
  
def isAuthenticated(f):
  @wraps(f)
  def decorator(*args, **kwargs):
    token = session.get('token')

    if not token:
      return redirect('/')
    
    verifyJWT(token)

    return f(*args, **kwargs)
  
  return decorator
