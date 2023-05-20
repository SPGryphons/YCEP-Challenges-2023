from flask import Flask, request, make_response, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/s3cr3t-p4gE-wottt')
def secret():
    cookie = request.cookies.get('cookie')
    if cookie == 'Chocolate Chip':
        return "<h1>Here's the flag: YCEP2023{5U5P1C10U5_BL0G_3XP053D}</h1>"
    else:
        res = make_response('''
        <h1>Intruder alert.</h1>
        <h2>Give me a Chocolate Chip cookie and we'll let you pass</h2>
        ''')

        if "cookie" not in request.cookies:
            res.set_cookie('cookie', 'none')
        return res


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=1337)    #modify if needed
