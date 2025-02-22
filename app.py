from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {username}'

@app.route('/data')
def data():
    return jsonify({'key': 'value3333'})

if __name__ == '__main__':
    app.run()