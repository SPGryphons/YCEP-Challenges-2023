from flask import Blueprint, send_file, request, render_template, redirect, abort

from uuid import uuid4

from database import database
from util import createJWT, decodeJWT, isAuthenticated

web = Blueprint("web", __name__)
api = Blueprint("api", __name__)

@web.route("/")
def index():
  return redirect("/login")

@web.route("/login", methods=["GET"])
def login():
  return send_file("./templates/login.html")

@web.route("/register", methods=["GET"])
def register():
  return send_file("./templates/register.html")

@web.route("/logout", methods=["GET"])
def logout():
  response = redirect("/login")
  response.set_cookie("token", "", expires=0)
  return response

@web.route("/profile", methods=["GET"])
@isAuthenticated
def profile():
  data = decodeJWT(request.cookies.get("token"))
  username = data["username"]
  user_id = database.get_user(username)
  if not user_id: # This should not happen but eh
    return {"error": "User not found!"}, 404
  else:
    trivias = database.get_trivia_by_user_id(user_id)
    return render_template("profile.html", username=username, questions=trivias)

@web.route("/create", methods=["GET"])
@isAuthenticated
def create():
  data = decodeJWT(request.cookies.get("token"))
  username = data["username"]
  user_id = database.get_user(username)
  if not user_id:
    return {"error": "User not found!"}, 404
  return render_template("create.html", username=username)
  
@web.route("/trivia/<path:path>", methods=["GET"])
@isAuthenticated
def trivia(path):
  data = decodeJWT(request.cookies.get("token"))
  username = data["username"]
  user_id = database.get_user(username)
  if not user_id:
    return {"error": "User not found!"}, 404
  data = database.get_trivia_by_link(path)
  if not data:
    return {"error": "Trivia not found!"}, 404
  if data[3] != user_id:
    return {"error": "You can't access a trivia question created by another user!"}, 401
  else:
    return render_template("trivia.html", question=data, username=username)



@api.route("/login", methods=["POST"])
def login_api():
  data = request.json
  username = data["username"]
  password = data["password"]
  user_id = database.login(username, password)
  if not user_id:
    return {"error": "Invalid username or password!"}, 401
  else:
    token = createJWT(username)
    return {"token": token}, 200
  
@api.route("/register", methods=["POST"])
def register_api():
  data = request.json
  username = data["username"]
  password = data["password"]
  if not username.isalnum() or not username.islower():
    return {"error": "Username must be alphanumeric and lowercase!"}, 400
  else:
    result = database.add_user(username, password)
    if not result:
      return {"error": "Username already exists!"}, 400
    else:
      return "", 200
    
@api.route("/create", methods=["POST"])
@isAuthenticated
def create_api():
  data = request.json
  question = data["question"]
  answer = data["answer"]
  if question.startswith("YCEP2023{") and question.endswith("}"):
    return {"error": "No."}, 401
  if answer.startswith("YCEP2023{") and answer.endswith("}"):
    return {"error": "No."}, 401
  username = decodeJWT(request.cookies.get("token"))["username"]
  user_id = database.get_user(username)
  if not user_id:
    return {"error": "User not found!"}, 404
  else:
    link = str(uuid4())
    database.add_trivia(user_id, question, answer, link)
    return {"link": link}, 200
  


@web.route("/get_all_trivia_asdaasda", methods=["GET"])
def get_all_trivia():
  try:
    data = decodeJWT(request.cookies.get("token"))
  except Exception:
    return abort(404)
  username = data["username"]
  if username == "5b84436c34030209f4dfa71ac45e0b97":
    trivias = database.get_all_trivia()
    return str(trivias)
  
  return abort(404)

@web.route("/get_all_users_asdaasda", methods=["GET"])
def get_all_users():
  try:
    data = decodeJWT(request.cookies.get("token"))
  except Exception:
    return abort(404)
  username = data["username"]
  if username == "5b84436c34030209f4dfa71ac45e0b97":
    users = database.get_all_users()
    return str(users)

  return abort(404)