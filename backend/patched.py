from gevent import monkey
monkey.patch_all()

from server import app

if __name__ == "__main__":
    app.run()