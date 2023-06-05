from flask import Flask, send_file, send_from_directory, request
import sqlite3 as sql
conn = sql.connect(":memory:", check_same_thread=False)

base = open("init.sql",'r').read()
cursor = conn.cursor()
cursor.executescript(base)
conn.commit()
cursor.close()

def userquery(q):
    try:
        cursor = conn.cursor()
        cursor.execute(q)
        response = cursor.fetchall()
        cursor.close()
        return response
    except sql.DatabaseError as e:
        print(e)
        return False
    
def anticheat(q):
    blacklist = ['insert','delete','alter','drop','sleep','create','into']
    for i in blacklist:
        if i in q:
            return False 
    else:
        return True

app = Flask(__name__)

@app.route("/",methods=["GET"])
def index():
    return send_file("index.html")

@app.route("/getItem",methods=["GET"])
def getItem():
    try:
        itemid = request.args.to_dict()['query']
        if anticheat(itemid):
            response = list(userquery(f'select * from items where id = {itemid};'))
            if response:
                return response
            else:
                return 'Not Found',400
            
        else:
            return 'Anticheat activated',400
        
    except:
        return 'Not Found',400


@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == 'GET':
        return send_file('login.html')
    else:
        arg = request.json 
        try:
            username = arg['username']
            password = arg['password']
            # lazy way of checking
            # no need hashlib or anyt
            if username == 'Administrator_0x1' and password == 'rocketman':
                return 'YCEP2023{SqL1_wAS_fUN_r1GHt}'
            
            else:
                return 'incorrect username/password',401    
        except:
            return 'bad request', 500

@app.route("/static/<path:path>")
def serve_all(path):
    return send_from_directory('static',path)

if __name__ == "__main__":
    app.run("0.0.0.0",1337,debug=True)
