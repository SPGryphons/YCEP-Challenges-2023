import base64
import sqlite3
from flask import Flask, request, render_template_string, g
app = Flask(__name__)

DATABASE = 'database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def return_index():
    secret_key = request.args.get('secret_key')
    if secret_key and base64.b64decode(secret_key).decode('utf-8') == 'opensesame':
        flag = 'YCEP2023{h1dd3n_g4t3w4y}'
    else:
        flag = None
    return render_template_string(open('../dist/index.html').read(), flag=flag)

@app.route('/check_user')
def check_user():
    username = request.args.get('username', '')
    password = request.args.get('password', '')
    db = get_db()
    user = db.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password)).fetchone()
    if user:
        return "Welcome back, {}".format(username)
    else:
        return "Invalid credentials"

if __name__ == '__main__':
    with app.app_context():
        db = get_db()
        db.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
        db.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("admin", "password"))
        db.commit()
    app.run(host='0.0.0.0', port=1337)