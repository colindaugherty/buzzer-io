from flask import Flask, Response
from flask_restplus import Api
from flask_socketio import SocketIO, send, emit
import pdb
import eventlet
eventlet.monkey_patch()

app = Flask(__name__)
api = Api(app)
socketio = SocketIO(app, message_queue='redis://redis:6379')

@app.route('/')
def get_domain():
    return Response('OK')

@socketio.on('connect')
def handle_connect():
    print('client connected')


@socketio.on('message')
def handle_message(message):
    emit('message', message, broadcast=True, json=True)


@socketio.on('disconnect')
def handle_disconnect():
    print('client disconnected')


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)