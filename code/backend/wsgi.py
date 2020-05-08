from gevent import monkey
monkey.patch_all()

from server import socketio, app

if __name__ == "__main__":
    socketio.run(app)