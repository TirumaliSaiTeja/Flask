# Dynamic URl Building

from flask import Flask, url_for
from werkzeug.utils import redirect

app = Flask(__name__)


@app.route('/admin')
def admin():
    return 'admin'

@app.route('/student')
def student():
    return 'student'

@app.route('/librarian')
def librarian():
    return 'librarian'

@app.route('/user/<name>')
def user(name):
    if name == 'admin':
        return redirect(url_for('admin'))
    if name == 'student':
        return redirect(url_for('student'))
    if name == 'librarian':
        return redirect(url_for('librarian'))
if __name__ == '__main__':
    app.run(debug=True)


