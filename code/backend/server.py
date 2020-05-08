from flask import Flask, flash, render_template, request, session, redirect, url_for, jsonify
from flask_socketio import SocketIO
from gevent import monkey
monkey.patch_all()

app = Flask(__name__)

app.config["SERVER_NAME"] = "buzz.colindaugherty.net"
app.config["SECRET_KEY"] = "sUP3R-S3cRE7_H4&H"

socketio = SocketIO(app, ping_timeout=120)

@app.route("/api")
def index():
    return render_template("api.html")

@app.route("/api/startGame/<int:gameID>")
def startGame(gameID):
    setUpDone = True
    return jsonify({'setUpDone' : setUpDone})

@app.route("/api/getPlayerList/<int:gameID>", methods=['GET'])
def getPlayerList(gameID):
    player_list = "Coming soon"
    return jsonify({'player_list' : player_list})

@app.route("/api/getPlayerBuzzes/<int:gameID>", methods=['GET'])
def getPlayerBuzzes(gameID):
    player_buzzes = "Coming soon"
    return jsonify({'player_buzzes' : player_buzzes})

@app.route("/api/updatePlayerList/<int:gameID>", methods=['PUT'])
def updatePlayerList(gameID):
    updatedList = []
    return jsonify({'updatedPlayerList' : updatedList})

@app.route("/api/deleteGame/<int:gameID>", methods=['DELETE'])
def deleteGame(gameID):
    deletedGame = True
    return jsonify({'deletedGame' : deletedGame})

@socketio.on('newPlayerJoined', namespace='/sockets')
def playerJoined(json):
    print("Got newPlayerJoined")
    room = json['room']
    player = json['player']
    print(f"Parsed data, name is {player} and room is {room}")
    socketio.emit('playerJoined', {'player' : str(player)}, room=room, namespace='/sockets')
    print("Sent")

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=5000)