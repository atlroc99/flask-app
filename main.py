from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World</h1>'


@app.route('/user/<name>')
def user(name):
    return f'Hello, user: {name}'


@app.route('/user/<int:id>')
def user_by_id(id):
    return f'found user for id: {id}'
