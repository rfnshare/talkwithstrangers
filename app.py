from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from datetime import datetime

app = Flask(__name__)
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('message')
def handle_message(data):
    message = data['msg']
    username = data['username']
    timestamp = data['timestamp']
    emit('message', {'username': username, 'msg': message, 'timestamp': timestamp}, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
