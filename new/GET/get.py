from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/login', methods = ['GET'])
def login():
    uname = request.args.get('uname')
    password = request.args.get('pass')
    if uname == 'Sai' and password == '123456':
        return 'Welcome %s' %uname

if __name__ == '__main__':
    app.run(debug=True)

