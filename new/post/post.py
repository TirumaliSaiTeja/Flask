from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods = ['POST'])
def login():
    uname = request.form['uname']
    password = request.form['pass']
    if uname == 'Sai' and password == '123456':
        return 'Welcome %s' %uname

if __name__ == '__main__':
    app.run(debug=True)

