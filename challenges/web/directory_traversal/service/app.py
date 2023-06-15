from flask import Flask, render_template, send_from_directory, request, send_file

app = Flask(__name__)


@app.route('/')
def index():
    # send from static
    return send_file('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return send_file('login.html')
    else:
        try:
            args = request.json
            if args['username'] == 'admin' and args['password'] == 'monke':
                return 'YCEP2023{L0GiN_pA9E_TR@VerSal}'
            else:
                return 'Wrong username or password'
        except:
            return 'Invalid request'

@app.route('/admin')
def admin():
    return send_file('admin.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337)
