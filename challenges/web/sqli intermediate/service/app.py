from flask import Flask, send_file, send_from_directory, request
import sqlite3 as sql
conn = sql.connect(":memory:", check_same_thread=False)

base = open("init.sql",'r').read()
cursor = conn.cursor()
cursor.executescript(base)
conn.commit()
cursor.close()
# http://127.0.0.1:9999/getItems?query=1%20UNION%20SELECT%20id,username,password,4%20FROM%20users;%20--

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

app = Flask(__name__)

@app.route("/",methods=["GET"])
def index():
    return send_file("index.html")

@app.route("/getItems",methods=["GET"])
def getItem():
    try:
        itemid = request.args.to_dict()['query']
        print(f'select * from items where id = {itemid};')
        response = userquery(f'select * from items where id = {itemid};')
        if response:
            return str(response)
        
        else:
            return 'err',400
    except:
        return 'err',400


@app.route("/login",methods=["POST"])
def login():
    arg = request.json 
    try:
        username = arg['username']
        password = arg['password']

        if username == 'Administrator_0x1' and password == 'rocketman':
            return 'YCEP2023{SqL1_wAS_fUN_r1GHt}'
        
        else:
            return 'incorrect username/password',401    
    except:
        return 'bad request', 500


@app.route("/static/<path:path>")
def serveall(path):
    return send_from_directory('static',path)


if __name__ == "__main__":
    app.run("127.0.0.1",9999,debug=True)
