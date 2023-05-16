from flask import Flask, request, render_template
from html import escape

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=["POST"])
def login_auth():

    try:
        username = escape(request.form['username'])
        password = escape(request.form['password'])
        role = escape(request.form['role'])

        if len(username) < 1:
            return "Please enter your username"
        
        if len(password) < 1:
            return "Please enter your password"
        
        text = f"<h1>Welcome, {role} {username}!</h1>"
        flag = "<h1>Here's your flag: YCEP2023{5N34KY_H1DD3N_1NPU7}</h1>"

        if role.lower() == 'guest':
            return text
        elif role.lower() == 'admin':
            return text + '<br><br>' + flag
        else: 
            return render_template('login.html')

    except:
        return render_template('login.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)