from flask import Flask
app = Flask(__name__)

app.config["SERVER_NAME"] = ["buzz.colindaugherty.net"]

@app.route("/api")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

@app.route("/api/tests")
def test():
    return "<h1 style='color:blue'>General Kenobi!</h1>"

if __name__ == "__main__":
    app.run()